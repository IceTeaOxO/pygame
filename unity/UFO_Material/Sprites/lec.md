# UFO初學者教學11/17<br/>
學習目標<br/>
1.使用鍵盤控制角色移動<br/>
2.蒐集物件Collider<br/>
3.分數Canvas<br/>

步驟:<br/>
1-放置背景、UFO=>圖層順序<br/>
2-讓UFO進行移動=>Start,Update,public, private , translate/addforce<br/>
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

3-camera調整<br/>
size,background<br/>

4-蒐集物件功能<br/>
為金塊、UFO加上rigibody 2D, circle collider 2D，將重力設為0<br/>
在UFO加上<br/>
public void OnCollisionEnter2D(Collision2D collision)
    {
        Debug.Log(collision.gameObject.tag);
    }
查看碰撞效果<br/>

破壞物件<br/>
Destroy(collision.gameObject);

5-建立UI text<br/>
建立金塊prefab<br/>
右鍵->UI->text (TMP)<br/>
調整位置、文字<br/>
using Text = TMPro.TextMeshProUGUI;<br/>

6-其他小細節<br/>
為牆壁加上collider<br/>
金塊自動產生<br/>
為UFO、金塊加上轉動效果-rotation<br/>

