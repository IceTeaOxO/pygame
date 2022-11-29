using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class action : MonoBehaviour
{
    private Animator Animator;
    public float moveSpeed = 0.1f;
    private SpriteRenderer mySpriteRenderer;

    // Start is called before the first frame update
    void Start()
    {
        Animator = GetComponent<Animator>();
        mySpriteRenderer = GetComponent<SpriteRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            mySpriteRenderer.flipX = true;
            Animator.SetInteger("state", 1);
            transform.position -= new Vector3(moveSpeed, 0);
        }
        else if (Input.GetKey(KeyCode.RightArrow))
        {
            mySpriteRenderer.flipX = false;
            Animator.SetInteger("state", 1);
            transform.position += new Vector3(moveSpeed, 0);
        }
        else
        {
           Animator.SetInteger("state", 0);
        }
    }
}
