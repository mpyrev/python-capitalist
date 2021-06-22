from capitalist import Capitalist


def test_get_documents_history(mocker):
    # Data for example on page https://capitalist.net/developers/api/page/get_documents_history_ext
    data = {
        "code": 0,
        "message": "",
        "data": {
            "pages": {
                "itemCount": 7,
                "pageCount": 1,
                "pageSize": 30,
                "currentPage": 0,
                "currentPageCount": 7
            },
            "history": [
                {
                    "number": 92362566,
                    "date": "22.01.2015 15:20:58",
                    "state": "Исполнен",
                    "corrDetails": "WebMoney: Z112224443331",
                    "comment": None,
                    "amount": "-1.40",
                    "description": "Payout 6",
                    "state_code": "EXECUTED"
                },
                {
                    "number": 92362498,
                    "date": "22.01.2015 15:20:57",
                    "state": "Исполнен",
                    "corrDetails": "WebMoney: Z112224443331",
                    "comment": None,
                    "amount": "-1.10",
                    "description": "Payout 3",
                    "state_code": "EXECUTED"
                },
                {
                    "number": 92362519,
                    "date": "22.01.2015 15:20:57",
                    "state": "Отменен",
                    "corrDetails": "WebMoney: Z112224443331",
                    "comment": "Внешний сервис вернул ошибку: корреспондент не найден",
                    "amount": "-1.20",
                    "description": "Payout 4",
                    "state_code": "DECLINED"
                },
                {
                    "number": 92362585,
                    "date": "22.01.2015 15:20:58",
                    "state": "Исполнен",
                    "corrDetails": "WebMoney: Z112224443331",
                    "comment": None,
                    "amount": "-1.50",
                    "description": "Payout 7",
                    "state_code": "EXECUTED"
                },
                {
                    "number": 92362544,
                    "date": "22.01.2015 15:20:57",
                    "state": "Исполнен",
                    "corrDetails": "WebMoney: Z112224443331",
                    "comment": None,
                    "amount": "-1.30",
                    "description": "Payout 5",
                    "state_code": "EXECUTED"
                }
            ]
        }
    }
    mocker.patch("capitalist.Capitalist.secure_request", return_value=data)

    assert len(data["data"]["history"]) == len(Capitalist(None, None).get_documents_history())
