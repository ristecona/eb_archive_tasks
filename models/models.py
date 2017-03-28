# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ArchiveTasksLine(models.TransientModel):

    _name = 'base.task.archive.line'
    _order = 'min_id asc'

    wizard_id = fields.Many2one('base.task.archive.automatic.wizard', 'Wizard')

class EbArchiveTasks(models.TransientModel):

    _name = 'base.task.archive.automatic.wizard'
    _description = 'Archive Tasks'

    @api.model
    def default_get(self, fields):
        res = super(EbArchiveTasks, self).default_get(fields)
        active_ids = self.env.context.get('active_ids')
        if self.env.context.get('active_model') == 'project.task' and active_ids:
            #res['state'] = 'selection'
            res['task_ids'] = active_ids
            #res['dst_task_id'] = self._get_ordered_partner(active_ids)[-1].id
        return res

    task_ids = fields.Many2many('project.task', 'merge_tasks_rel', 'merge_id', 'task_id', string='Tasks')



    @api.multi

    def action_archive(self):
        self.task_ids.write({'active': False})
        return True
