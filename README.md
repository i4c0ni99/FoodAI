## Titolo

**FoodAI - Progetto per il corso di Intelligenza Artificiale**

## Descrizione

Il progetto è stato concepito per semplificare la pianificazione dei pasti quotidiani in modo altamente personalizzato. 
Il fabbisogno nutrizionale giornaliero dell'utente viene calcolato e gestito in cinque pasti: colazione, spuntino mattutino, pranzo, spuntino pomeridiano e cena. 
Attraverso un'interfaccia grafica, l'utente inserisce informazioni personali per calcolare il fabbisogno calorico giornaliero (TDEE)

FoodAI utilizza questi dati per generare un piano alimentare su misura, dettagliando esattamente quali alimenti consumare e in che quantità. 
Se un alimento suggerito non è di gradimento o non è disponibile, consente di richiedere facilmente un'alternativa, senza compromettere gli obiettivi nutrizionali. 


## Caratteristiche Principali

- **Personalizzazione**: raccomandazioni basate sulle preferenze dell'utente e possibilità di modificare gli alimenti proposti
- **Flessibilità**: gestione di vari vincoli nutrizionali
- **Efficienza**: utilizzo di tecniche di Machine Learning e CSP per generare i piani alimentari
- **Interfaccia intuitiva**: frontend per un'interazione semplice e user-friendly

## Struttura del Progetto

- **/**: script python per la preparazione del dataset, l'addestramento e il CSP
- **/csv**: contiene le varie versioni del dataset (grezzo, processato, trainato) e file di appoggio
- **/json**: contiene il tracker dei feedback sull'addestramento e l'output del validator del CSP
- **/stats**: grafici e statistiche relative all'addestramento
- **/static**: contiene il CSS e le utils
- **/templates**: contiene le pagine HTML

## Requisiti


Per eseguire questo progetto, è necessario installare i pacchetti Python presenti nel 
file requirements.txt:

```
pip install -r requirements.txt
```
 
## Istruzioni per l'uso

1. **Preparazione del dataset**:
   - Eseguire lo script `dataset_maker.py` per ottenere il dataset preprocessato
   - Eseguire lo script `nutra.py` per calcolare il punteggio nutrizionale basato sulla regressione lineare

2. **Avvio del sistema**:
   - Eseguire:
     ```
     uvicorn requestFE:app --reload
     ```
   - Avviare il frontend:
     ```
     Aprire `localhost:8000` nel browser e inserire le informazioni richieste.
     ```

3. **Generazione del piano alimentare**:
   - Inserire le informazioni personali tramite la form nell'interfaccia.
   - Selezionare almeno cinque categorie alimentari.
   - Confermare per ottenere il piano alimentare personalizzato.

## Contributi

Siamo aperti a contributi esterni, puoi creare un branch e proporre modifiche tramite una pull request.

## Licenza

Questo progetto è distribuito sotto licenza MIT.

---

A cura di:  
**Luigi Iaconi**  
**Luca Visconti**

---
