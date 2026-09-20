label junior_route_start:
    scene bg university_common
    show junior fullbody_default at fullbody_fit
    with fade

    narrator "【유나 루트】"
    junior "선배는 제가 왜 여기 온 건지 정말 모르세요?"
    p "설마 나 때문이라고 하려는 건 아니지?"
    show junior fullbody_shy at fullbody_fit
    junior "그 설마가 맞아요."

    menu:
        "그 마음을 가볍게 넘기지 않고 현재의 유나를 보겠다고 한다.":
            $ junior_reassurance += 1
            $ junior_affection += 10
            p "과거 때문에 책임지는 척은 안 할게. 대신 지금부터 제대로 볼게."
            show junior fullbody_flustered at fullbody_fit
            junior "...그 말, 취소하면 안 돼요."

        "부담스럽다고 거리를 둔다.":
            p "그건 좀... 무겁다."
            show junior fullbody_hurt at fullbody_fit
            junior "그렇죠. 선배한테는."

    show junior fullbody_jealousy at fullbody_fit
    narrator "며칠 뒤 유나는 하린과의 관계를 조심스럽게 캐묻기 시작했다."

    menu:
        "불안하면 직접 물어보라고 하고 관계를 명확히 한다.":
            $ junior_reassurance += 1
            p "혼자 추측하지 마. 궁금하면 나한테 물어봐."
            show junior fullbody_shy at fullbody_fit
            junior "그럼... 저만 좋아한다고 말해 주세요."
            p "그래."

        "괜히 싸우기 싫어 대답을 피한다.":
            p "그런 것까지 설명해야 해?"
            show junior fullbody_anger at fullbody_fit
            junior "...알겠어요. 제가 알아서 할게요."

    if junior_reassurance >= 4:
        jump junior_happy
    else:
        jump junior_bad

label junior_happy:
    scene bg university_common
    show junior fullbody_default at fullbody_fit
    narrator "도서관 폐관 방송이 나온 뒤."
    show junior fullbody_joy at fullbody_fit
    junior "예전에는 선배를 따라오기만 했어요."
    p "이제는?"
    junior "옆에서 갈래요."
    p "그래. 그게 낫다."
    $ ending_seen = "junior_happy"
    centered "YUNA HAPPY END\n따라가는 사람이 아니라"
    return

label junior_bad:
    scene black
    narrator "처음엔 사소했다."
    narrator "누구와 밥을 먹었는지, 왜 답장이 늦었는지, 하린과 무슨 이야기를 했는지."
    narrator "어느 순간부터 유나는 내가 누구와 만날지 먼저 알고 있었다."
    junior "선배. 그 사람하고는 이제 연락 안 하시는 게 좋을 것 같아요."
    p "유나야. 내 휴대폰 봤어?"
    junior "왜요? 숨길 게 있어요?"
    narrator "익숙하던 미소가 처음으로 낯설게 보였다."
    $ ending_seen = "junior_bad"
    centered "YUNA BAD END\n나만 보면 되잖아요"
    return
