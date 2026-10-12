# 橋牌叫牌教學影片

台灣繁體中文的橋牌叫牌教學素材，內容只講叫牌：叫品的意義、判斷，以及同伴間的資訊溝通。
觀眾須先懂基本打牌規則；還不熟的話，可以先看[冷光橋藝教室第一級](https://www.youtube.com/watch?v=F2aTonsHemI)。

叫牌制度與術語依作者的文字教材 [bridge-tutorial](https://github.com/jdh8/bridge-tutorial) 核對。

## 內容

- [`pilot/`](pilot/)：試作「1♥ 到底代表什麼？」，共九張 1080×1080 圖卡與旁白稿。
  編修與轉檔流程見 [`pilot/使用說明.txt`](pilot/使用說明.txt)。

系列的分集、順序與媒介尚未定案。

## 產生圖卡

需要 Inkscape、Noto Sans CJK TC 字型與 Python。

```sh
pip install -r requirements.txt
python3 pilot/make_frames.py
```

SVG 是畫面的原稿；`pilot/png/` 與 `pilot/overview.jpg` 由程式產生，不納入 Git。

## 授權

Copyright (c) 2026 Chen-Pang He。

- 程式碼（`*.py`）採 MIT 授權，全文見 [LICENSE-MIT](LICENSE-MIT)。
- 其餘文稿、圖卡及其衍生的圖片、錄音與影片，採
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hant) 授權，全文見 [LICENSE](LICENSE)。
