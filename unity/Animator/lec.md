## 2D animator
<br/>
一個角色身上只會有一個animator
一個animator可以有多組的animation

### key設定
-create new clip
做動畫要先選時間軸才會有影格
增加關鍵動作或效果要ADD KEY
動畫靠每個KEY紀錄的數值去調整組件
--DopeSheet
--Curves

--Set as Layer Default State
--Make Transition
--Parameters/Animator.setInteger("stateName",value)
--Has Exit Time
--ctrl+6/windows

### 步驟<br/>
為圖片增加animator，進入animation增加clip<br/>
將圖片拖進clip點擊play播放<br/>
在animator整理動作間的關係以及切換方式<br/>
使用make transition建立動作間的關聯，進入parameter設定切換動作的條件參數<br/>
然後點擊連接動作的線，新增條件參數<br/>
加上修改參數的script，微調細節<br/>

#### code<br/>
--SpriteRenderer圖片物件<br/>
--myAnimator動畫物件/scale X<br/>

#### unity asset


### 骨骼動畫補充教材<br/>
https://www.youtube.com/watch?v=LNqr7K_7cx0<br/>
https://www.mixamo.com/#/<br/>
## Animator Controller參考資料<br/>
https://www.cg.com.tw/Unity/Content/Unity_21.php<br/>