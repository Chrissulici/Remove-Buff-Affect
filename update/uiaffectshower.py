#search in def __init__(self):
		if app.ENABLE_AFFECT_BUFF_REMOVE:
			self.buffQuestionDialog = None
			self.skillIndex = None
			
#add:
			self.SetEvent(ui.__mem_func__(self.OnBuffQuestionDialog), "MOUSE_LEFT_BUTTON_UP")
			
#search:
		def OnBuffQuestionDialog(self, skillIndex):
			self.buffQuestionDialog = uiCommon.QuestionDialog()
			self.buffQuestionDialog.SetWidth(350)
			self.buffQuestionDialog.SetText(localeInfo.BUFF_AFFECT_REMOVE_QUESTION % (skill.GetSkillName(skillIndex)))
			self.buffQuestionDialog.SetAcceptEvent(lambda arg = skillIndex: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.SetCancelEvent(lambda arg = 0: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.Open()
			
#replace:
		def OnBuffQuestionDialog(self):
			skillIndex = self.skillIndex
			if not skillIndex or skillIndex == 66:
				return
			self.buffQuestionDialog = uiCommon.QuestionDialog()
			self.buffQuestionDialog.SetWidth(350)
			self.buffQuestionDialog.SetText(localeInfo.BUFF_AFFECT_REMOVE_QUESTION % (skill.GetSkillName(skillIndex)))
			self.buffQuestionDialog.SetAcceptEvent(lambda arg = skillIndex: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.SetCancelEvent(lambda arg = 0: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.Open()
			
#search in def OnMouseOverIn(self) and delete:
		if app.ENABLE_AFFECT_BUFF_REMOVE:
			if self.skillIndex:
				self.OnBuffQuestionDialog(self.skillIndex)