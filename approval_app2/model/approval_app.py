from odoo import models, fields,api, _

class ApprovalApp(models.Model):
    _name='approval.app'

    name=fields.Char('Name')
    submission_date=fields.Datetime('Submission Date')
    admin_officer=fields.Char('Admin Officer')
    admin_appro_date=fields.Datetime('Admin Approval Date')
    osd_officer_one=fields.Selection([('kim_possible', 'Kim Possible'), ('john_brown', 'John Brown')], string='OSD Officer')
    date_osd_officer_assigned=fields.Datetime('Date OSD Officer Assigned')
    date_approved_by_ocd_officer=fields.Datetime('Date Approved by OSD Officer')
    date_sent_to_lead_group=fields.Datetime('Date sent to Lead Group')
    date_appro_by_lead_group=fields.Datetime('Date Approved by Lead Group')
    date_sent_to_council=fields.Datetime('Date sent to Council')
    date_return_from_council=fields.Datetime('Date returned from Council')
    relese_date_to=fields.Datetime('Release Date To')
    job_title=fields.Char('Job Title')
    purpose_job=fields.Char('Purpose of Job	')
    level=fields.Selection([],string='Level')
    modality=fields.Selection([('ato', 'ATO'), ('internal', 'Internal')], string='Modality')
    no_of_person=fields.Integer('Number of persons expected to be trained')

    lead_group_member=fields.One2many('group.member','app_id',string='Lead Group Member	')
    contact =fields.Many2one('res.partner',string='Contact')
    office_phone=fields.Char('Office Phone')
    cell_phone=fields.Char('Cell Phone')
    email=fields.Char('Email')
    address=fields.Char('Address')
    industry=fields.Many2one('industry.company')
    sub_sector=fields.Many2one('sub.sector')
    date=fields.Date('Date')
    staff_headcount=fields.Integer('Staff Headcount	')
    vale_attr=fields.Text('Values and attitudes	')
    job_task=fields.One2many('task.description','app_1_id')
    stage_id=fields.Many2one('approval.stage')



class GroupMember(models.Model):
    _name='group.member'

    app_id=fields.Many2one('approval.app')
    name=fields.Char('Name')
    email=fields.Char('Email')
    contact=fields.Char('Contact')
    title = fields.Char('Title')


class IndustryCompany(models.Model):
    _name='industry.company'

    name=fields.Char('Name')


class SubSector(models.Model):
    _name = 'sub.sector'

    name = fields.Char('Name')


class TaskDescription(models.Model):
    _name='task.description'

    name=fields.Char('Job Tasks')
    detail_task=fields.Char('Details Of Task')
    app_1_id=fields.Many2one('approval.app')


class ApprovalStage(models.Model):
    _name='approval.stage'

    name=fields.Char('Name')


