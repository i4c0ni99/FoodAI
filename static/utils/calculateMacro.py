def calculate_kal_macro(data):
    activity_factor = None

    # Definire il fattore di attività in base allo stile di vita
    if data['stile_di_vita'] == 'sedentario':
        activity_factor = 1.0
    elif data['stile_di_vita'] == 'attivo':
        activity_factor = 1.55
    elif data['stile_di_vita'] == 'molto attivo':
        activity_factor = 1.75
    else:
        raise ValueError("Livello di attività non valido")

    # Calcolo del BMR
    bmr = 10 * data['peso'] + 6.25 * data['altezza'] - 5 * data['eta'] + 5
    tdee = bmr * activity_factor

    # Calcolo delle percentuali di macronutrienti e TDEE aggiornato in base all'obiettivo
    macro = calculate_macronutrient_percentages(data['stile_di_vita'], tdee, data['obbiettivo'])
    carb_g = macro['carb_g']
    protein_g = macro['protein_g']
    fat_g = macro['fat_g']
    tdee = macro['tdee']

    # Assegnazione delle calorie per ogni pasto
    colazione = spuntino_mat = pranzo = spuntino_pom = cena = None
    if data['numero_di_pasti'] == 5:
        colazione = tdee * 0.20
        spuntino_mat = tdee * 0.07
        pranzo = tdee * 0.35
        spuntino_pom = tdee * 0.08
        cena = tdee * 0.30
    else:
        raise ValueError("Numero pasti non consentito")

    pasti = {
        'colazione': colazione,
        'spuntino_mat': spuntino_mat,
        'pranzo': pranzo,
        'spuntino_pom': spuntino_pom,
        'cena': cena
    }

    return {
        'tdee': tdee,
        'protein_g': protein_g,
        'carb_g': carb_g,
        'fat_g': fat_g,
        'pasti': pasti
    }


def calculate_macronutrient_percentages(stile_di_vita, tdee, goal):
    # Definire percentuali di macronutrienti in base all'obiettivo
    protein_percentage = carb_percentage = fat_percentage = None

    if goal == 'dimagrimento':
        if stile_di_vita == 'sedentario':
            carb_percentage = 0.3
            protein_percentage = 0.4
            fat_percentage = 0.3
        elif stile_di_vita == 'attivo':
            carb_percentage = 0.35
            protein_percentage = 0.4
            fat_percentage = 0.25
        elif stile_di_vita == 'molto attivo':
            carb_percentage = 0.40
            protein_percentage = 0.35
            fat_percentage = 0.25
        else:
            raise ValueError("Livello di attività non valido")
        tdee -= 500  # Calorie ridotte per dimagrimento

    elif goal == 'mantenimento':
        if stile_di_vita == 'sedentario':
            carb_percentage = 0.45
            protein_percentage = 0.30
            fat_percentage = 0.20
        elif stile_di_vita == 'attivo':
            carb_percentage = 0.50
            protein_percentage = 0.25
            fat_percentage = 0.25
        elif stile_di_vita == 'molto attivo':
            carb_percentage = 0.50
            protein_percentage = 0.25
            fat_percentage = 0.25
        else:
            raise ValueError("Livello di attività non valido")

    elif goal == 'massa':
        tdee += 500  # Calorie aumentate per aumento di massa
        if stile_di_vita == 'sedentario':
            carb_percentage = 0.5
            protein_percentage = 0.3
            fat_percentage = 0.2
        elif stile_di_vita == 'attivo':
            carb_percentage = 0.55
            protein_percentage = 0.30
            fat_percentage = 0.15
        elif stile_di_vita == 'molto attivo':
            carb_percentage = 0.55
            protein_percentage = 0.30
            fat_percentage = 0.15
        else:
            raise ValueError("Livello di attività non valido")

    else:
        raise ValueError("Obiettivo non valido")

    # Calcolo dei macronutrienti in grammi
    protein_g = protein_percentage * tdee / 4
    carb_g = carb_percentage * tdee / 4
    fat_g = fat_percentage * tdee / 9

    return {
        'tdee': tdee,
        'protein_g': protein_g,
        'carb_g': carb_g,
        'fat_g': fat_g
    }
