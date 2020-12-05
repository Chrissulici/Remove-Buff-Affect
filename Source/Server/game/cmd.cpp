//search:
struct command_info cmd_info[] =

//add before:
#ifdef ENABLE_AFFECT_BUFF_REMOVE
ACMD(do_remove_buff);
#endif

//search:
	{	"\n",							NULL,							0,						POS_DEAD,			GM_IMPLEMENTATOR	}

//add before:
#ifdef ENABLE_AFFECT_BUFF_REMOVE
	{	"remove_buff",					do_remove_buff,					0,						POS_DEAD,			GM_IMPLEMENTATOR	},
#endif