# Unity 2D
https://www.cg.com.tw/Unity2D/

# UFO初學者教學
學習目標
1.使用鍵盤控制角色移動
2.蒐集物件Collider
3.分數Canvas

步驟:
1-放置背景、UFO=>圖層順序
2-讓UFO進行移動=>Start,Update,public, private , translate/addforce
public float speed;

    private Rigidbody2D rb2d;
    private int count;

//rb2d = GetComponent<Rigidbody2D>();


private void FixedUpdate()
    {
        float moveH = Input.GetAxis("Horizontal");
        float moveV = Input.GetAxis("Vertical");
        Vector2 movement = new Vector2 (moveH, moveV);
        this.transform.Translate(movement * Time.deltaTime);
        //rb2d.AddForce (movement*speed);
    }

3-camera調整
size,background

4-蒐集物件功能
建立金塊prefab
collider






## asset store
UFO _Complete-Game
sunny land

window->asset store->sunnt land
window->package manager->my asset->download & import 

## prefab

## Animator Controller

https://www.cg.com.tw/Unity/Content/Unity_21.php

## C# script

https://www.cg.com.tw/UnityCSharp/

## camera

## collision/trigger

## material

physics material

## audio

## UI

## unity play / webgl / manage project file




# Unity 3D
## 地形製作
## 光源設定
## 環境設定
## 匯入檔案
## 角色製作
## 粒子系統
## 影像效果
## 角色動畫

https://www.cg.com.tw/Unity/Content/Unity_22.php

## navmesh 自動尋路
## 布料模擬
## Mixamo角色動作
## Unity 常見錯誤
https://www.cg.com.tw/Unity2D/