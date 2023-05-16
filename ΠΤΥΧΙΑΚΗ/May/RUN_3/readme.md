# Περιγραφή
**Σκοπός:** 
Σκοπός της εργασίας είναι η ανάπτυξη ενός chatbot που να απαντά ερωτήσεις των χρηστών για Πρώτες Βοήθειες.

**Λειτουργία:** 
Το Chabot δέχεται ως είσοδο κείμενο και προβλέπει μεταξύ 267 διαφορετικών προθέσεων την πρόθεση της ερώτησης της εισόδου με τη χρήση ενός προεκπαιδευμένου μοντέλου. Έπειτα, εμφανίζει στην οθόνη του χρήστη την απάντηση. Σε περίπτωση που η καλύτερη πρόβλεψη έχει πιθανότητα μικρότερη του 0.5, τότε εμφανίζεται ως απάντηση ότι η ερώτηση του χρήστη δεν είναι επαρκής. 

**Εκπαίδευση**
- Φόρτωση δεδομένων εκπαίδευσης και επικύρωσης
- Προεπεξεργασία Φυσικής Γλώσσας:
  - Αφαίρεση σημείων στίξεως και χαρακτήρα newline
  - Tokenization: Διαχωρισμός κάθε ερωτήσης σε λίστα λέξεων
  - Lemmatization:

**Υπό Ανάτυξη**
- Web Εφαρμογή

## Αρχεία
- ```training.py``` :   Εκπαίδευση μοντέλου του chatbot
- ```chatbot.py``` :  Chatbot Interface για την επικοινωνία των χρηστών με το chatbot
- ```output.txt``` :  Αποτελέσματα ερωτήσεις-απαντήσεις του chatbot (πηγή ερωτήσεων: ```training_data_3.txt```) και αξιολόγηση ορθότητας
- ```training_data_3.txt``` : Περιέχει το σύνολο των δεδομένων εκπαίδευσης με τη μορφή (αριθμός_ερώτησης\n ερώτηση\n απάντηση)
- ```validation_data_3.txt``` : Περιέχει το σύνολο των δεδομένων επικύρωσηw με τη μορφή (αριθμός_ερώτησης\n ερώτηση\n απάντηση)

## Βάση γνώσης


## Jupyter Notebook
- https://github.com/lextale/Uni-Assignments/blob/main/ΠΤΥΧΙΑΚΗ/May/RUN_3/training.ipynb
- https://github.com/lextale/Uni-Assignments/blob/main/ΠΤΥΧΙΑΚΗ/May/RUN_3/chatbot.ipynb

## Στατιστικά
**Model Training Accuracy**

![Model Training Accuracy](https://github.com/lextale/Uni-Assignments/blob/main/ΠΤΥΧΙΑΚΗ/May/RUN_3/model_3_accuracy.png)

**Model Training Loss**

![Model Training Loss](https://github.com/lextale/Uni-Assignments/blob/main/ΠΤΥΧΙΑΚΗ/May/RUN_3/model_3_loss.png)
