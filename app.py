from flask import Flask, request

import resend

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    resend.api_key = "re_JKZNXV2a_PP8L16LCXAuAWDPZFtH3uqMD"
    po = request.json.get("po")
    organization = request.json.get("organization")
    review_url = request.json.get("review_url")

    params = {
        "from": "onboarding@resend.dev",
        "to": ["zach@tryresponse.com"],
        "subject": f"[PLEASE CONFIRM] PO #{po} from {organization}",
        "html": f"""
            <p>{organization} sent you a purchase order!</p>
            <p>Purchase Order #{po}</p>
            <p><b>Please review purchase order below.</b></p>
            <br>
            <br>
            <p style="text-align: center">
            <a href="{review_url}" style="background: #2F64ED; padding: 25px; color: white; font-size: 15pt; border-radius: 7px; text-decoration: none;">
            Review Purchase Order
            </a>
            </p>
            <br>
        """,
        "reply_to": "keivan@tryresponse.com",
    }

    return resend.Emails.send(params)
