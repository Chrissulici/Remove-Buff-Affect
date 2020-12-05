//search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 0);
#endif

//add:
#ifdef ENABLE_AFFECT_BUFF_REMOVE
	PyModule_AddIntConstant(poModule, "ENABLE_AFFECT_BUFF_REMOVE", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_AFFECT_BUFF_REMOVE", 0);
#endif