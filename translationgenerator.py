import pandas as pd

KEYNAMES_NEWRESERVATION = ["Neue Reservierung","Patientendaten",
            "Name","Vorname","Titel","Geburtsdatum","Geburtsort","Geschlecht",
            "Nationalität","Sprache", "Hauptadresse und Kontaktdaten",
            "Länderkennzeichen","Postleitzahl","Ort","Straße und Hausnummer", 
            "Festnetz","Fax","Mobilnummer","Email","Persönliche Angaben",
            "Beruf","Behinderung","Foto erlaubt", "Anreise", "Ankunft", "Bemerkung Fallbezogen",
            "Sonstiges", "Strukturierte Patienteninfo", "Medizinische Vorabinformation", 
            "Gästebetreuung", "Marketing", "Medizinische Vorabinformation", "Gästebetreuung"
            ]

KEYNAMES_GUEST = [
    "Dear", "we have just received your registration for your stay from","to", "at our clinic in", 
    "Thank you very much for providing your information and your time.\nNow we can perfectly prepare your stay. Enclosed you will find a summary of the data we have saved at our internal servers. Please let us know if any information changes or is incorrect.",
    "Contact Details", "We’re happy to welcome you again in our house.",
    "Your personal Information", "Name", "Gender", "Date of birth", "Place of birth", "Job", "Nationality", "Language(s)", 
    "Talk", "Your Contact Information", "Email", "Address", "Phone", "Other Phone", "Fax", "Emergency Contact",
    "Your Stay", "Reason for the stay", "Arrival", "Departure", "Media", "Therapy Wish", "Your health Information",
    "Weight", "Height", "Allergies", "Support needed", "Contraindicative diseases", "Medication", "Covid test result",
    "Covid symptoms","Further Information", "Recommendation by", "Given consent", "Filled out date",
    "Is anything wrong or should be changed? Let us know via"
            
            ]

fakedf = [
    ["German"] + KEYNAMES_NEWRESERVATION,
    ["English"] + KEYNAMES_NEWRESERVATION,
    ["Spanish"] + KEYNAMES_NEWRESERVATION,
    ["French"] + KEYNAMES_NEWRESERVATION
]
columnnames = ["Language"] + list(range(len(KEYNAMES_NEWRESERVATION)))
reservationdf = pd.DataFrame(fakedf, columns=columnnames)
reservationdf = reservationdf.set_index("Language")
reservationdf.to_json("translations/reservationmail_translations.json", orient='index', indent=2)
reservationdf.to_excel("translations/reservationmail_translations.xlsx")

fakedf = [
    ["German"] + KEYNAMES_GUEST,
    ["English"] + KEYNAMES_GUEST,
    ["Spanish"] + KEYNAMES_GUEST,
    ["French"] + KEYNAMES_GUEST
]
columnnames = ["Language"] + list(range(len(KEYNAMES_GUEST)))
reservationdf = pd.DataFrame(fakedf, columns=columnnames)
reservationdf = reservationdf.set_index("Language")
reservationdf.to_json("translations/guestmail_translations.json", orient='index', indent=2)
reservationdf.to_excel("translations/guestmail_translations.xlsx")