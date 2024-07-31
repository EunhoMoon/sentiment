from google.cloud import language_v2
from google.protobuf.json_format import MessageToDict


class Analyze:
    def __init__(self):
        self._client = language_v2.LanguageServiceClient()
        self._document_type = language_v2.Document.Type.PLAIN_TEXT
        self._language_code = "ko"

    def analyze_sentiment_from_text(self, text_content: str) -> dict:
        try:
            document = {
                "content": text_content,
                "type_": self._document_type,
                "language_code": self._language_code,
            }

            encoding_type = language_v2.EncodingType.UTF8

            response = self._client.analyze_sentiment(
                request={"document": document, "encoding_type": encoding_type}
            )
            response_dict = MessageToDict(response._pb)

            result = {
                "score": response_dict["documentSentiment"]["score"],
                "magnitude": response_dict["documentSentiment"]["magnitude"],
            }
        except Exception as e:
            result = {"error": str(e)}

        return result
