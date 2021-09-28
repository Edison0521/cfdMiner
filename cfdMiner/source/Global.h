#pragma once 

#include <stdio.h>

#define INT_BIT_LEN	32

#define ITEM_SUP_MAP_SIZE   1000

#define MAX_FILENAME_LEN	100
#define MAX(x,y)   (x>=y?x:y)
#define MIN(x,y)   (x<=y?x:y)


//parameter settings
extern int gnmin_sup;

//some statistic information about the data
extern int gndb_size;
extern int gnmax_trans_len;
extern int gnmax_item_id;

//pattern statistics
extern int  gntotal_freqitems;
extern int	gnmax_pattern_len;
extern int gntotal_singlepath;
extern int gntotal_generators;
extern int gntotal_closed;


//time statistics
extern double gdtotal_running_time;

//space statistics
extern double gdused_mem_size;
extern double gdmax_used_mem_size;
extern int gntree_init_size;
extern int gntree_max_size;

//program running statistics
extern int gntotal_call;
extern int gngenerator_check_times;

int comp_int_asc(const void *e1, const void *e2);

void MineFreqGenerators();
void PrintSummary();

//global varibles
extern int *gpprefix_itemset;
extern int gnprefix_len;
extern int *gpfull_itemset;
extern int gnfull_len;
extern int gnglobal_full;



extern int *gptransaction;
extern char *gpsort_trans_buf;
extern int gnum_of_newfreqitems;

extern int *gpdfs_item_suporder_map;
extern char *gpitem_bitmap;
extern char *gpclosed_bitmap;

extern int *gpsingle_branch;


struct ITEM_COUNTER
{
	int nitem;
	int norder;
	int nsupport;
};

extern ITEM_COUNTER *gpdfs_item_counter;