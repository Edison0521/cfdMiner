#include <string.h>

#include "parameters.h"
#include "Global.h"

CParameters goparameters;


void CParameters::SetResultName(char *szresult_name)
{
	sprintf(szgenerator_filename, "%s.key.txt", szresult_name);
	sprintf(szclosed_filename, "%s.closed.txt", szresult_name);
	sprintf(szpair_filename, "%s.pair.txt", szresult_name);
}

