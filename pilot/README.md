# 圖卡試作：1♥ 到底代表什麼？

2026-10-12 先把原有 9 張影片畫面改成 1080×1080 的正方形圖卡。
保留原本配色與教學順序，重新安排斷行與字級；圖卡本身就寫出每張的重點。
本組只教叫品的字面意思：線位、花色或無王、目標磴數。
這次是媒介試作，整個系列的形式與順序仍未定案。

## 檔案

| 路徑 | 說明 |
| --- | --- |
| `svg/` | 畫面的唯一來源；文字、斷行、配色與版面直接在 SVG 編修 |
| `make_frames.py` | 只讀取 SVG，轉成 PNG 並製作總覽；不存放圖卡文案或版面 |
| `png/` | 9 張 1080×1080 圖卡，按檔名 01–09 排序（產生檔，不納入 Git） |
| `overview.jpg` | 全部畫面的縮圖總覽（產生檔，不納入 Git） |
| `../備份/pilot-影片版-20261012.tar.gz` | 本機備份，不納入 Git；包含改版前的程式、旁白稿與 1920×1080 圖片 |

## 教材來源

取材自 [bridge-tutorial](https://github.com/jdh8/bridge-tutorial/blob/main/src/auction.md) 的「叫品」與「合約、莊家、夢家」，只介紹叫品的字面意思。
開叫所需的牌力、牌型與同伴間的約定留到後續；本組圖卡不示範出牌。

## 預覽與使用

先執行轉檔，再看 `overview.jpg` 的九張總覽與 `png/` 內的單張原圖確認文字。
製作輪播貼文時，依 01–09 的順序選取 PNG。

- 01 提問，02–04 逐步解釋，05 換成無王。
- 06 練習，07 揭曉答案。
- 08 整理規則，09 銜接叫牌的資訊溝通。

目前尚未上傳到任何平台。

## 貼文說明

以下文字可直接貼在貼文或影片說明：

```text
本系列聚焦叫牌，預設你已懂基本打牌規則。
需要補出牌規則、主打與防禦，請參考冷光橋藝教室：
https://www.youtube.com/watch?v=F2aTonsHemI
影片說明列有第一級課程；第 1 集是出牌規則，第 3 集是基本主打，第 4 集是防禦基本觀念。

圖卡：Chen-Pang He，CC BY 4.0（https://creativecommons.org/licenses/by/4.0/deed.zh-hant）
```

## 編修畫面

- 用 Inkscape 或文字編輯器直接修改 `svg/` 對應檔；SVG 是 single source of truth。
- PNG 與總覽是衍生檔，編修請回到 SVG。
- 匯出全部圖卡：在專案根目錄執行 `python3 pilot/make_frames.py`（在 `pilot/` 則執行 `python3 make_frames.py`）。
- 指令依 SVG 檔名排序，按原稿的頁面尺寸以 96 dpi 匯出同名 PNG，再更新 `overview.jpg`。
- 只覆寫 `png/` 中的同名檔案與 `overview.jpg`，不改動 SVG 原稿。
- 增減圖卡時，直接在 SVG 更新頁碼與總張數；轉檔程式不會修改畫面。
- 刪除或更名 SVG 後，舊 PNG 需自行移除；轉檔程式不刪除檔案。
- 轉檔需要 Python、Pillow、Inkscape 與 Noto Sans CJK TC 字型；安裝方式見[根目錄 README](../README.md)。

## 授權

圖卡採 CC BY 4.0，`make_frames.py` 採 MIT，詳見[根目錄 README](../README.md#授權)。
單獨分享圖卡時，在說明中寫上「Chen-Pang He，CC BY 4.0」與授權連結即可，不必隨附 LICENSE 全文。
冷光等外部教材、字型與第三方套件維持各自授權。
