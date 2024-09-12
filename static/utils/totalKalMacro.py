def kilototal(colazione, spuntino_mat, pranzo, spuntino_pom, cena):
    if colazione and spuntino_mat and pranzo and spuntino_pom and cena:
        total_kcal = (
            colazione['carbohydrate']['kilocalories'] + colazione['fat']['kilocalories'] + colazione['protein']['kilocalories'] +
            spuntino_mat['carbohydrate']['kilocalories'] + spuntino_mat['fat']['kilocalories'] + spuntino_mat['protein']['kilocalories'] +
            pranzo['carbohydrate']['kilocalories'] + pranzo['fat']['kilocalories'] + pranzo['protein']['kilocalories'] +
            spuntino_pom['carbohydrate']['kilocalories'] + spuntino_pom['fat']['kilocalories'] + spuntino_pom['protein']['kilocalories'] +
            cena['carbohydrate']['kilocalories'] + cena['fat']['kilocalories'] + cena['protein']['kilocalories']
        )
        return round(total_kcal, 2)
    return 0
def totalCarb(colazione, spuntino_mat, pranzo, spuntino_pom, cena):
    if colazione and spuntino_mat and pranzo and spuntino_pom and cena:
        total_kcal = (
            colazione['carbohydrate']['carbohydrate'] + colazione['fat']['carbohydrate'] + colazione['protein']['carbohydrate'] +
            spuntino_mat['carbohydrate']['carbohydrate'] + spuntino_mat['fat']['carbohydrate'] + spuntino_mat['protein']['carbohydrate'] +
            pranzo['carbohydrate']['carbohydrate'] + pranzo['fat']['carbohydrate'] + pranzo['protein']['carbohydrate'] +
            spuntino_pom['carbohydrate']['carbohydrate'] + spuntino_pom['fat']['carbohydrate'] + spuntino_pom['protein']['carbohydrate'] +
            cena['carbohydrate']['carbohydrate'] + cena['fat']['carbohydrate'] + cena['protein']['carbohydrate']
        )
        return round(total_kcal, 2)
    return 0
def totalFat(colazione, spuntino_mat, pranzo, spuntino_pom, cena):
    if colazione and spuntino_mat and pranzo and spuntino_pom and cena:
        total_kcal = (
            colazione['carbohydrate']['fat'] + colazione['fat']['fat'] + colazione['protein']['fat'] +
            spuntino_mat['carbohydrate']['fat'] + spuntino_mat['fat']['fat'] + spuntino_mat['protein']['fat'] +
            pranzo['carbohydrate']['fat'] + pranzo['fat']['fat'] + pranzo['protein']['fat'] +
            spuntino_pom['carbohydrate']['fat'] + spuntino_pom['fat']['fat'] + spuntino_pom['protein']['fat'] +
            cena['carbohydrate']['fat'] + cena['fat']['fat'] + cena['protein']['fat']
        )
        return round(total_kcal, 2)
    return 0
def totalProt(colazione, spuntino_mat, pranzo, spuntino_pom, cena):
    if colazione and spuntino_mat and pranzo and spuntino_pom and cena:
        total_kcal = (
            colazione['carbohydrate']['protein'] + colazione['fat']['protein'] + colazione['protein']['protein'] +
            spuntino_mat['carbohydrate']['protein'] + spuntino_mat['fat']['protein'] + spuntino_mat['protein']['protein'] +
            pranzo['carbohydrate']['protein'] + pranzo['fat']['protein'] + pranzo['protein']['protein'] +
            spuntino_pom['carbohydrate']['protein'] + spuntino_pom['fat']['protein'] + spuntino_pom['protein']['protein'] +
            cena['carbohydrate']['protein'] + cena['fat']['protein'] + cena['protein']['protein']
        )
        return round(total_kcal, 2)
    return 0