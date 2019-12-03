# LangDetector

API to detect language

## TOC

- [Routes](#)
  - [Detection Routes](#detection-routes)


## Routes

### Detection Routes

#### Overview

| Method |        URL         |     What to do     |
| :----: | :----------------: | :----------------: |
|  POST  | /api/v1/langdetect | Language detection |

#### Example

**POST /api/v1/langdetect **

```shell
$ curl http://127.0.0.1:8000/api/v1/langdetect \
	-X POST \
	-H 'content-type: application/json' \
	-d '{
          "sentence": "あなたはどうですか？"
        }
```

```shell
$ {
	"lang":"JP"
}
```
