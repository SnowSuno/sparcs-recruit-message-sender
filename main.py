from flask import Flask, redirect, request
import os

app = Flask(__name__)


def message(name: str, accept: bool):
    if accept:
        return \
            f"안녕하세요, {name} 님. SPARCS입니다.\n" \
            f"2023년 봄학기 SPARCS 리크루팅에 지원해 주셔서 감사드립니다.\n" \
            f"\n" \
            f"{name} 님은 2023년 봄학기 SPARCS 신입 회원으로 선발되셨습니다.\n" \
            f"합격을 진심으로 축하드립니다.\n" \
            f"앞으로 SPARCS의 일원으로서 뜻깊은 시간 함께 할 수 있기를 기원합니다.\n" \
            f"\n" \
            f"정기 모임 및 신입 회원 OT에 참석해 주시기를 바랍니다.\n" \
            f"시각: 23.03.06 (월) 오후 9시\n" \
            f"장소: 교양분관 1층 SPARCS 동아리방\n" \
            f"\n" \
            f"SPARCS 회장 황제욱 드림"
    else:
        return \
            f"안녕하세요, {name} 님. SPARCS입니다.\n" \
            f"2023년 봄학기 SPARCS 리크루팅에 지원해 주셔서 감사드립니다.\n" \
            f"\n" \
            f"{name} 님은 2023년 봄학기 SPARCS 신입 회원으로 선발되지 않으셨습니다.\n" \
            f"예상보다 많은 지원자들로 인해 모실 수 없게 되어 매우 안타깝게 생각합니다.\n" \
            f"추후 좋은 기회로 다시 만나뵐 수 있기를 기대하며, SPARCS에 관심 가져 주셔서 진심으로 감사드립니다.\n" \
            f"\n" \
            f"SPARCS 회장 황제욱 드림"


@app.route('/')
def do_redirect():
    phone, name, accept = request.args.get('phone'), request.args.get('name'), request.args.get('accept')

    if not phone or not name or not accept or accept not in ['합격', '불합격']:
        return "Bad request parameters", 400

    return redirect(f"sms://{phone}?&body={message(name, accept == '합격')}")


app.run(host="0.0.0.0", port=os.environ.get('PORT'))
