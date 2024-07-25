from fastapi import FastAPI
from google.cloud import language_v2
from google.protobuf.json_format import MessageToDict

app = FastAPI()


def sample_analyze_sentiment(text_content: str = "I am so happy and joyful.") -> dict:
    try:
        client = language_v2.LanguageServiceClient()

        document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

        language_code = "ko"
        document = {
            "content": text_content,
            "type_": document_type_in_plain_text,
            "language_code": language_code,
        }

        encoding_type = language_v2.EncodingType.UTF8

        response = client.analyze_sentiment(
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


@app.get("/get_sentiment")
def get_sentiment():
    contents = """
        파라미터는 db에서 읽을 content의 key 값
        contents는 db에서 읽어온 텍스트 데이터
        """
    return sample_analyze_sentiment(text_content=contents)


@app.get("/")
def index():
    return {"message": "Hello, World!"}
