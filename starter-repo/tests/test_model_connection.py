"""Kiểm hợp đồng API bằng phản hồi giả lập; không phải kết quả eval model thật."""
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codebase"))
import ai
import tracing


class ModelConnectionTests(unittest.TestCase):
    def setUp(self):
        for key, value in {"MODEL_PROVIDER": "openai", "MODEL_NAME": "test-model",
                           "API_KEY": "test-secret", "MODEL_TIMEOUT": 30}.items():
            context = patch.object(ai, key, value)
            context.start()
            self.addCleanup(context.stop)

    def test_openai_usage_and_trace(self):
        response = {"model": "resolved-model", "choices": [{"finish_reason": "stop",
            "message": {"content": '{"label":"thieu_can_cu"}'}}],
            "usage": {"prompt_tokens": 20, "completion_tokens": 12,
                      "completion_tokens_details": {"reasoning_tokens": 5}}}
        tracing.begin("adapter-test")
        with patch.object(ai, "post_json", return_value=response) as post:
            result = ai.call_model("Return JSON", "claim")
        summary, _ = tracing.end()
        self.assertEqual(result["model"], "resolved-model")
        self.assertEqual((summary["tokens_in"], summary["tokens_out"]), (20, 12))
        self.assertEqual(summary["model_calls"], 1)
        self.assertEqual(post.call_args.args[2]["response_format"], {"type": "json_object"})

    def test_gemini_adds_separate_thinking_tokens(self):
        response = {"modelVersion": "resolved-gemini", "candidates": [{"finishReason": "STOP",
            "content": {"parts": [{"text": "private thought", "thought": True}, {"text": "{}"}]}}],
            "usageMetadata": {"promptTokenCount": 30, "candidatesTokenCount": 10, "thoughtsTokenCount": 7}}
        with patch.object(ai, "MODEL_PROVIDER", "gemini"), patch.object(ai, "post_json", return_value=response) as post:
            result = ai.call_model("system", "nhận định")
        self.assertEqual((result["tokens_in"], result["tokens_out"], result["text"]), (30, 17, "{}"))
        self.assertNotIn("test-secret", post.call_args.args[0])
        self.assertEqual(post.call_args.args[1]["x-goog-api-key"], "test-secret")

    def test_ollama_needs_no_key(self):
        response = {"done": True, "model": "local-model", "message": {"content": "{}"},
                    "prompt_eval_count": 8, "eval_count": 3}
        with patch.object(ai, "MODEL_PROVIDER", "ollama"), patch.object(ai, "API_KEY", ""), \
                patch.object(ai, "post_json", return_value=response):
            result = ai.call_model("system", "claim")
        self.assertEqual((result["tokens_in"], result["tokens_out"]), (8, 3))

    def test_missing_usage_is_not_estimated(self):
        response = {"choices": [{"finish_reason": "stop", "message": {"content": "{}"}}]}
        with patch.object(ai, "post_json", return_value=response), self.assertRaises(KeyError):
            ai.call_model("system", "claim")

    def test_truncated_output_is_error(self):
        response = {"choices": [{"finish_reason": "length", "message": {"content": "{"}}]}
        with patch.object(ai, "post_json", return_value=response), self.assertRaises(ValueError):
            ai.call_model("system", "claim")

    def test_missing_key_does_not_call_api(self):
        with patch.object(ai, "API_KEY", ""), patch.object(ai, "post_json") as post:
            with self.assertRaisesRegex(ValueError, "API_KEY"):
                ai.call_model("system", "claim")
        post.assert_not_called()

    def test_invalid_token_count(self):
        for value in (-1, True, "12", 1.5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                ai._tokens({"count": value}, "count")

    def test_http_error_hides_key_and_response(self):
        error = urllib.error.HTTPError("https://example.invalid/?key=test-secret", 401,
                                       "test-secret", {}, None)
        with patch.object(ai.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(RuntimeError) as caught:
                ai.post_json("https://example.invalid", {}, {})
        self.assertIn("401", str(caught.exception))
        self.assertNotIn("test-secret", str(caught.exception))

    def test_transport_sends_utf8_json_and_timeout(self):
        with patch.object(ai.urllib.request, "urlopen") as urlopen:
            urlopen.return_value.__enter__.return_value.read.return_value = b'{"ok":true}'
            self.assertEqual(ai.post_json("https://example.invalid", {}, {"claim": "Tiếng Việt"}), {"ok": True})
        request = urlopen.call_args.args[0]
        self.assertEqual(json.loads(request.data), {"claim": "Tiếng Việt"})
        self.assertEqual(urlopen.call_args.kwargs["timeout"], 30)


if __name__ == "__main__":
    unittest.main()
