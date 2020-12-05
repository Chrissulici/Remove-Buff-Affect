#search def __init__(self)::
		self.isClocked = True

#add:
		if app.ENABLE_AFFECT_BUFF_REMOVE:
			self.buffQuestionDialog = None
			self.skillIndex = None
			
#search:
	def SetSkillAffectFlag(self, flag):
		self.isSkillAffect = flag

#add:
	if app.ENABLE_AFFECT_BUFF_REMOVE:
		def SetSkillIndex(self, skillIndex):
			self.skillIndex = skillIndex
			
#search:
	def OnMouseOverIn(self):

#add before:
	if app.ENABLE_AFFECT_BUFF_REMOVE:
		def OnBuffQuestionDialog(self, skillIndex):
			self.buffQuestionDialog = uiCommon.QuestionDialog()
			self.buffQuestionDialog.SetWidth(350)
			self.buffQuestionDialog.SetText(localeInfo.BUFF_AFFECT_REMOVE_QUESTION % (skill.GetSkillName(skillIndex)))
			self.buffQuestionDialog.SetAcceptEvent(lambda arg = skillIndex: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.SetCancelEvent(lambda arg = 0: self.OnCloseBuffQuestionDialog(arg))
			self.buffQuestionDialog.Open()
			
		def OnCloseBuffQuestionDialog(self, answer):
			if not self.buffQuestionDialog:
				return

			self.buffQuestionDialog.Close()
			self.buffQuestionDialog = None

			if not answer:
				return

			net.SendChatPacket("/remove_buff %d" % answer)
			return TRUE
			
#search:
	def OnMouseOverIn(self):
		if self.toolTipText:
			self.toolTipText.Show()

#add:
		if app.ENABLE_AFFECT_BUFF_REMOVE:
			if self.skillIndex:
				self.OnBuffQuestionDialog(self.skillIndex)
				
#search:
		image.SetSkillAffectFlag(TRUE)
		image.SetDescription(name)

#add:
		if app.ENABLE_AFFECT_BUFF_REMOVE:
			image.SetSkillIndex(skillIndex)
				
