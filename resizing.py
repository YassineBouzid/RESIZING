"""MACHINE = db.Column(db.String(200),nullable=False)
    N_TUBE = db.Column(db.String(200),nullable=False)
    FAB_DATE = db.Column(db.String(200),nullable=False)
    FAB_POST = db.Column(db.String(200),nullable=False)
    FOURNISSEUR = db.Column(db.String(200),nullable=False)
    BOBINE = db.Column(db.String(200),nullable=False)
    COULEE = db.Column(db.String(200),nullable=False)
    PROJET = db.Column(db.String(200),nullable=False)
    DIAMETRE = db.Column(db.String(200),nullable=False)
    NUANCE = db.Column(db.String(200),nullable=False)
    EPAISSEUR = db.Column(db.String(200),nullable=False)
    VISUAL = db.Column(db.String(200),nullable=False)
    LONG_VISUEL = db.Column(db.String(200),nullable=False)
    VISA_VISUEL = db.Column(db.String(200),nullable=False)
    REPARATION = db.Column(db.String(200),nullable=False)
    VISA_REPARATION = db.Column(db.String(200),nullable=False)
    CHUTE = db.Column(db.String(200),nullable=False)
    VISA_CHUTE = db.Column(db.String(200),nullable=False)
    HYDRO = db.Column(db.String(200),nullable=False)
    VISA_HYDRO = db.Column(db.String(200),nullable=False)
    K_UT = db.Column(db.String(200),nullable=False)
    OPR_UT = db.Column(db.String(200),nullable=False)
    VISA_UT = db.Column(db.String(200),nullable=False)
    RX2 = db.Column(db.String(200),nullable=False)
    VISA_RX2 = db.Column(db.String(200),nullable=False)
    CN = db.Column(db.String(200),nullable=False)
    VISA_CN = db.Column(db.String(200),nullable=False)
    R_EPAISSEUR = db.Column(db.String(200),nullable=False)
    R_D_DIAMETER = db.Column(db.String(200),nullable=False)
    R_F_DIAMETER = db.Column(db.String(200),nullable=False)
    R_LONGEUR = db.Column(db.String(200),nullable=False)
    R_EPAISSEUR = db.Column(db.String(200),nullable=False)
    NEMERO_DE_RECEPTION = db.Column(db.String(200),nullable=False)
    R_VISA = db.Column(db.String(200),nullable=False)
    VISA_CLIENT = db.Column(db.String(200),nullable=False)
    TUBE_BLOQUEE = db.Column(db.String(200),nullable=False)
.replace("False","True"))
"""

carte = ["MACHINE", "N_TUBE","FAB_DATE","FAB_POST","FOURNISSEUR",
         "BOBINE","COULEE","PROJET","DIAMETRE", "NUANCE",
         "EPAISSEUR","VISUAL","LONG_VISUEL","VISA_VISUEL","REPARATION","VISA_REPARATION",
         "CHUTE","VISA_CHUTE","HYDRO","VISA_HYDRO","K_UT","OPR_UT","VISA_UT","RX2","VISA_RX2","CN","VISA_CN",
         "R_EPAISSEUR","R_D_DIAMETER","R_F_DIAMETER","R_LONGEUR","R_EPAISSEUR","NEMERO_DE_RECEPTION","R_VISA","VISA_CLIENT","TUBE_BLOQUEE"]



columns=[]

for name in carte:
    
    conlumn = f'{name} = StringField("{name}", validators=[DataRequired()])'
    
    columns.append(conlumn)
print((str(columns).replace(",",'\n')).replace("'",''))




























