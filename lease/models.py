from lease import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)
    rate = db.Column(db.Numeric(2,10), nullable=False)
    lease_fee = db.Column(db.Integer, nullable=False)
    init_fee = db.Column(db.Integer, nullable=True)
    deposit = db.Column(db.Integer, nullable=True)
    rstr_alwn = db.Column(db.Integer, nullable=True)
    basenode_id = db.Column(db.Integer)
    leasecls_id = db.Column(db.Integer, db.ForeignKey('leasecls.id', ondelete='CASCADE'), nullable=False)
    leasecls = db.relationship('Leasecls', backref=db.backref('contract_set'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('contract_set'))
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)

class Baseline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id', ondelete='CASCADE'))
    contract = db.relationship('Contract', backref=db.backref('baseline_set'))
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)
    rate = db.Column(db.Numeric(2,10), nullable=False)
    lease_fee = db.Column(db.Integer, nullable=False)
    init_fee = db.Column(db.Integer, nullable=True)
    deposit = db.Column(db.Integer, nullable=True)
    rstr_alwn = db.Column(db.Integer, nullable=True)
    prnt_asset = db.Column(db.Integer, nullable=True)
    prnt_depac = db.Column(db.Integer, nullable=True)
    prnt_lblti = db.Column(db.Integer, nullable=True)
    prnt_dpsit = db.Column(db.Integer, nullable=True)
    prnt_rstra = db.Column(db.Integer, nullable=True)
    basenode_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('baseline_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cycle = db.Column(db.Integer, nullable=True)
    exemonth = db.Column(db.Date, nullable=False)           #????????????
    lease_fee = db.Column(db.Integer, nullable=True)        #??? ?????????
    lease_lbt = db.Column(db.Integer, nullable=True)        #????????????
    lease_exp = db.Column(db.Integer, nullable=True)        #????????????
    deposit_dscnt = db.Column(db.Integer, nullable=True)    #????????? ?????????
    deposit_intr = db.Column(db.Integer, nullable=True)     #???????????????
    rstr_exp = db.Column(db.Integer, nullable=True)         #?????????????????? ?????????
    rstr_alw = db.Column(db.Integer, nullable=True)         #??????????????????
    lease_dep = db.Column(db.Integer, nullable=True)        #???????????????
    dep_accum = db.Column(db.Integer, nullable=True)        #?????????????????????
    lease_ast = db.Column(db.Integer, nullable=True)        #?????????????????????(??????-????????????)
    lease_acq = db.Column(db.Integer, nullable=True)        #?????????????????????
    inhr = db.Column(db.Integer, nullable=True)             #????????????
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id', ondelete='CASCADE'), nullable=True)
    contract = db.relationship('Contract', backref=db.backref('schedule_set'))
    baseline_id = db.Column(db.Integer, db.ForeignKey('baseline.id', ondelete='CASCADE'), nullable=True)
    baseline = db.relationship('Baseline', backref=db.backref('schedule_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Leasecls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clsname = db.Column(db.String(150), unique=True, nullable=False)
