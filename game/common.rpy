label common_day1:
    scene bg event_harin_commute
    with fade

    narrator "【월요일 / 복학 첫날】"
    p "학교가 이렇게 낯설었나."
    p "군대 가기 전에는 매일 오던 곳인데."

    narrator "정문으로 이어지는 등교길은 기억보다 넓고, 사람들의 걸음은 기억보다 빨랐다."
    narrator "그 틈에서 누군가 자연스럽게 내 보폭에 맞춰 걸어왔다."
    friend "야. 설마 진짜 혼자 다니려고 했어?"
    p "...하린?"
    friend "복학생이라고 벌써부터 분위기 잡지 마. 밥부터 먹자."

    menu:
        "하린을 따라가 학생식당에 간다.":
            $ friend_affection += 10
            $ friend_courage += 1
            p "그래. 혼자 먹는 것보단 낫겠지."
            friend "그 말투 뭐야. 그냥 반가웠다고 해."

        "일단 학과사무실부터 가겠다고 한다.":
            p "복학 서류부터 처리해야 해."
            friend "하여튼 변한 게 없네. 끝나면 연락해."

    call screen chapter_transition("화요일 / 학과사무실", "파티션 너머에서 마주친 조교")
    jump common_day2

label common_day2:
    scene bg event_seoyun_office
    with fade

    narrator "【화요일 / 학과사무실】"

    narrator "파티션 너머로 내민 복학 서류가 잠깐 허공에 머물렀다."
    narrator "모니터를 보던 조교가 고개를 돌리자 은색 포니테일과 동그란 안경이 먼저 눈에 들어왔다."
    older "복학 처리 서류... 여기 확인해 주세요."
    p "감사합니다. 조교님이시죠?"
    older "네. 서윤이라고 합니다."
    p "생각보다 어려 보이시네요."
    older "......그런 말 자주 하세요?"
    p "아뇨. 방금 처음 했는데요."
    older "아. 네. 그렇군요."

    narrator "업무 이야기는 멀쩡하게 하던 사람이 갑자기 시선을 피한다."

    menu:
        "괜히 부담 주지 않고 서류 이야기로 돌아간다.":
            $ older_affection += 10
            $ older_trust += 1
            p "제가 확인할 건 이것뿐이죠?"
            older "네. ...감사합니다."

        "왜 갑자기 피하냐고 묻는다.":
            $ older_affection += 5
            p "혹시 제가 불편하게 했어요?"
            older "아니에요. 그런 건 아닌데..."

    call screen chapter_transition("수요일 / 강의 후 강의실 앞", "초저녁 복도에서 기다리던 후배")
    jump common_day3

label common_day3:
    scene bg event_yuna_classroom
    with fade

    narrator "【수요일 / 강의 후 강의실 앞】"

    narrator "마지막 강의가 끝나자 복도에는 초저녁의 어둠이 천천히 내려앉고 있었다."
    narrator "강의실 문을 나서자 가로등 불빛 옆에 서 있던 누군가가 조심스럽게 고개를 들었다."
    junior "선배."
    p "...나 부른 거야?"
    junior "네. 저 기억 안 나세요?"
    p "잠깐. 유나?"
    junior "다행이다. 아예 잊은 줄 알았어요."

    narrator "고등학교 때 몇 번 마주쳤던 두 살 어린 후배."
    narrator "그 애가 같은 대학 교정에 서 있었다."

    menu:
        "먼저 연락하지 그랬냐고 반갑게 말한다.":
            $ junior_affection += 10
            $ junior_reassurance += 1
            p "같은 학교면 먼저 연락하지 그랬어."
            junior "...해도 됐어요?"
            p "당연하지."

        "어떻게 이 학교에 왔는지 묻는다.":
            $ junior_affection += 5
            p "근데 네가 여기 올 줄은 몰랐다."
            junior "저는 알고 있었어요. 선배가 여기 다니는 거."

    call screen chapter_transition("목요일 / 빈 세미나실", "서윤의 이상한 거짓말")
    jump common_day4

label common_day4:
    scene bg university_common
    narrator "【목요일 / 빈 세미나실】"

    show older fullbody_default at fullbody_fit
    with dissolve
    older "아, 맞다. 교수님이 찾으세요."
    p "저를요? 지금요?"
    older "네. 아마... 지금이요."
    hide older

    narrator "교수실까지 올라갔지만 교수는 영문을 몰랐다."
    prof "내가 자네를 왜 찾아?"
    p "......"
    narrator "그제야 알았다."
    narrator "서윤 조교는 나를 피하려고 거짓말까지 한 것이다."

    menu:
        "다음에 만나도 모른 척해준다.":
            $ older_affection += 10
            $ older_trust += 1
            p "...뭔가 사정이 있겠지."

        "바로 학과사무실로 돌아가 따진다.":
            $ older_affection += 5
            p "이건 좀 너무한데."

    call screen chapter_transition("금요일 / 하린과 귀가 중", "친구라는 말의 거리")
    jump common_day5

label common_day5:
    scene bg university_common
    narrator "【금요일 / 하린과 귀가 중】"

    show friend fullbody_default at fullbody_fit
    with dissolve
    friend "아 맞다. 지난번에 아는 언니 따라갔다가 다른 학교 선배 하나 알게 됐거든."
    p "남자?"
    friend "왜, 궁금해?"

    menu:
        "조금 신경 쓰인다고 솔직하게 말한다.":
            $ friend_affection += 10
            $ friend_courage += 1
            p "응. 조금은."
            friend "...오. 군대 갔다 오더니 이런 말도 하네?"

        "관심 없는 척한다.":
            $ friend_affection += 5
            p "네가 누구를 만나든 네 자유지."
            friend "그렇긴 하지."

    hide friend
    call screen chapter_transition("다음 주 / 도서관", "유나가 꺼낸 저녁 약속")
    jump common_day6

label common_day6:
    scene bg university_common
    narrator "【다음 주 / 도서관】"

    show junior fullbody_default at fullbody_fit
    with dissolve
    junior "선배. 오늘 저녁 시간 있으세요?"
    p "왜?"
    junior "밥 먹고 싶어서요. 선배랑."

    menu:
        "약속을 잡는다.":
            $ junior_affection += 10
            $ junior_reassurance += 1
            p "그래. 수업 끝나고 보자."
            junior "...네. 꼭이요."

        "다음에 보자며 애매하게 넘긴다.":
            $ junior_affection += 5
            p "이번 주는 좀 애매하다. 다음에 보자."
            junior "다음이 언제인데요?"
            p "정해지면 연락할게."
            junior "...알겠어요."

    hide junior
    call screen chapter_transition("축제 준비 주간", "겹치기 시작한 세 사람의 시간")
    jump common_day7

label common_day7:
    scene bg university_common
    narrator "【축제 준비 주간】"
    narrator "셋과 보내는 시간이 겹치기 시작했다."

    menu:
        "학과사무실에 남아 서윤의 일을 도와준다.":
            $ older_affection += 10
            $ older_trust += 1
            p "저도 할 일 없는데 도와드릴게요."

        "하린과 축제 준비를 한다.":
            $ friend_affection += 10
            $ friend_courage += 1
            p "이번엔 내가 같이 갈게."

        "유나와 도서관에서 과제를 한다.":
            $ junior_affection += 10
            $ junior_reassurance += 1
            p "오늘은 안 미룰게. 같이 하자."

    call screen chapter_transition("공통 루트 종료", "이제 누구에게 마음을 향할지 정할 시간")
    jump route_selection

label route_selection:
    scene bg university_common
    narrator "공통 루트 종료"
    narrator "서윤 호감도: [older_affection] / 하린 호감도: [friend_affection] / 유나 호감도: [junior_affection]"
    narrator "호감도 20 이상인 히로인의 개별 루트에 진입할 수 있습니다."

    menu:
        "서윤과 더 가까워진다" if older_affection >= 20:
            $ selected_route = "older"
            call screen chapter_transition("서윤 루트", "도망가려는 사람에게 다가가는 법")
            jump older_route_start

        "하린과 더 가까워진다" if friend_affection >= 20:
            $ selected_route = "friend"
            call screen chapter_transition("하린 루트", "친구 다음의 이름")
            jump friend_route_start

        "유나와 더 가까워진다" if junior_affection >= 20:
            $ selected_route = "junior"
            call screen chapter_transition("유나 루트", "오래 기다린 마음")
            jump junior_route_start

        "누구와도 관계를 정하지 않는다":
            call screen chapter_transition("노멀 엔딩", "아무 말도 하지 않은 가을")
            jump neutral_ending

label neutral_ending:
    scene bg university_common
    narrator "나는 결국 아무에게도 마음을 전하지 않았다."
    narrator "복학 첫 학기는 그렇게 평범하게 흘러갔다."
    centered "NORMAL END\n아무 말도 하지 않은 가을"
    return
