class Variables:
  def __init__(self, app_id=None, owner_id=None, hash=None):
    self.days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    self.pics_days = {
      0: "photo-193457847_457239037",
      1: "photo-193457847_457239038",
      2: "photo-193457847_457239039",
      3: "photo-193457847_457239040",
      4: "photo-193457847_457239041",
      5: "photo-193457847_457239042",
      6: "photo-193457847_457239043"}
    self.pics_beer = {
      0: "photo-193457847_457239044",
      1: "photo-193457847_457239045",
      2: "photo-193457847_457239046",
      3: "photo-193457847_457239047",
      4: "photo-193457847_457239048",
      5: "photo-193457847_457239050"}
    self.dice_var = {
      0: "photo-193457847_457239156",
      1: "photo-193457847_457239157",
      2: "photo-193457847_457239158",
      3: "photo-193457847_457239159",
      4: "photo-193457847_457239160",
      5: "photo-193457847_457239161"
    }
    self.coin = {
      0: "photo-193457847_457239162",
      1: "photo-193457847_457239163",
      2: "photo-193457847_457239192"
    }
    self.notifications =[
      '@all',
      '*all',
      '@все',
      '*все'
    ]
    self.empty_keyboard = {
      "one_time": False,
      "buttons": []
    }
    self.keyboard = [[{
                        "color": "positive",
                        "action": {
                            "type": "text",
                            "label": "🍺 Пивко 🍺",
                            "payload": {
                              "command": "beer"
                            }
                        }
                    }, 
                    {
                        "color": "positive",
                        "action": {
                            "type": "text",
                            "label": "3=Размер члена=э",
                            "payload": {
                              "command": "penis"
                            }
                        }
                    },
                    {
                        "color": "positive",
                        "action": {
                            "type": "text",
                            "label": "🏳️‍🌈 Тест на гея 🏳️‍🌈",
                            "payload": {
                              "command": "gaytest"
                            }
                        }  
                    }
                   ],
                   [
                     {
                        "color": "positive",
                        "action": {
                            "type": "text",
                            "label": "♂ Гачи тест ♂",
                            "payload": {
                              "command": "gachitest"
                            }
                        }  
                      },
                      {
                          "color": "positive",
                          "action": {
                              "type": "text",
                              "label": "🎲Кости🎲",
                              "payload": {
                                "command": "dice"
                              }
                          }  
                        },
                       {
                          "color": "positive",
                          "action": {
                              "type": "text",
                              "label": "🪙Монетка🪙",
                              "payload": {
                                "command": "coin"
                              }
                          }  
                      }
                   ],
                    [
                      {
                        "color": "negative",
                        "action": {
                            "type": "text",
                            "label": "Скрыть",
                            "payload": {
                              "command": "hide"
                            }
                        }  
                      },
                      {
                        "action": {
                          "type": "open_app",
                          "app_id": app_id,
                          "owner_id": owner_id,
                          "hash": str(hash),
                          "label": "Донат"
                        }
                      }
                    ]
                  ]
    # self.donation_btn = [
    # ]
    self.gachi_pics = {
      0: {
        "photo": "photo-73192688_456251828",
        "name": "Billy Herrington"
      },
      1: {
        "photo": "photo-73192688_412965053",
        "name": "Danny Lee"
      },
      2: {
        "photo": "photo-73192688_412965122",
        "name": "Van Darkholme"
      },
      3: {
        "photo": "photo-73192688_412970676",
        "name": "Brian Maxon"
      },
      4: {
        "photo": "photo-73192688_412965031",
        "name": "Cameron Sage"
      },
      5: {
        "photo": "photo-73192688_412965033",
        "name": "Aleksander Vishnevskiy"
      },
      6: {
        "photo": "photo-73192688_412965034",
        "name": "Stevie Cassidy"
      },
      7: {
        "photo": "photo-73192688_412965037",
        "name": "Jirka Kalvoda"
      },
      8: {
        "photo": "photo-73192688_412965044",
        "name": "Christian Engel"
      },
      9: {
        "photo": "photo-73192688_412965061",
        "name": "Ron Athey"
      },
      10: {
        "photo": "photo-73192688_412965065",
        "name": "ChiChi La Rue"
      },
      11: {
        "photo": "photo-73192688_412965084",
        "name": "Blake Harper"
      },
      12: {
        "photo": "photo-73192688_412965118",
        "name": "Colton Ford"
      },
      13: {
        "photo": "photo-73192688_412965089",
        "name": "Anthony Stone"
      },
      14: {
        "photo": "photo-73192688_412965091",
        "name": "Steve Grier"
      },
      15: {
        "photo": "photo-73192688_412965095",
        "name": "Ricardo Milos"
      },
      16: {
        "photo": "photo-73192688_412965099",
        "name": "Anthoney Capriatti"
      },
      17: {
        "photo": "photo-73192688_412965106",
        "name": "Bo Garrett"
      },
      18: {
        "photo": "photo-73192688_456251826",
        "name": "Steve Rambo"
      },
    }
    self.verdicts_m = [
      "не гей", 
      "латентный гей", 
      "бисексуал", 
      "полупокер", 
      "конкретный пидорас", 
      "ебучая пидорасня"]
    self.verdicts_w = [
      "не лесбиянка", 
      "латентная лесбиянка", 
      "бисексуал_ка", 
      "любительница вагин", 
      "тру лесбиянка", 
      "анти-хуй"]