import gspread


def add_user(user):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open_by_key('1XYRJnTcr9mo9SDpLC1ZTdOwcOJLsRNNx0vMx1M2YacU')
    worksheet = sh.sheet1
    worksheet.append_row(user)

