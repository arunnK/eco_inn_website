import django_tables2 as tables
from pages.models import Member

class MemberTable(tables.Table):
    class Meta:
        model = Member
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
