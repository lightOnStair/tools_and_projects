#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashmap.h"

long hashcode(char key[]){
  union {
    char str[8];
    long num;
  } strnum;
  strnum.num = 0;

  for(int i=0; i<8; i++){
    if(key[i] == '\0'){
      break;
    }
    strnum.str[i] = key[i];
  }
  return strnum.num;
}

void hashmap_init(hashmap_t *hm, int table_size){
  hm->item_count = 0;
  hm->table_size = table_size;
  hm->table = malloc(sizeof(hashnode_t)*table_size);
  for(int i=0; i<table_size;i++){
    hm->table[i] = NULL;
  }
}

int hashmap_put(hashmap_t *hm,char key[], char val[]){
  int index = hashcode(key) % (hm->table_size);

  hashnode_t *temp = hm->table[index];
  if(temp==NULL){
    hashnode_t *new = malloc(sizeof(hashnode_t));
    strcpy(new->key,key);
    strcpy(new->val,val);
    new->next = NULL;
    hm->table[index] = new;
    hm->item_count += 1;
    return 1;
  }
  while(temp!=NULL){
    if(strcmp(temp->key,key)==0){
      strcpy(temp->val,val);
      return 0;
    }
    else if(temp->next==NULL){
      hashnode_t *new = malloc(sizeof(hashnode_t));
      strcpy(new->key,key);
      strcpy(new->val,val);
      new->next = NULL;
      temp->next = new;
      hm->item_count += 1;
    }
    else{
    temp = temp->next;
    }
  }
  return 1;
}

char *hashmap_get(hashmap_t *hm, char key[]){
  int index = hashcode(key) % hm->table_size;

  hashnode_t *temp = hm->table[index];
  while(temp!=NULL){
    if(strcmp(temp->key,key)==0){
      char *val = temp->val;
      return val;
    }
    else{
      temp = temp->next;
    }
  }
  return NULL;
}

void hashmap_free_table(hashmap_t *hm) {
	int len = hm->table_size;
  hashnode_t *temp;
	for(int i = 0; i < len; i++) {
		hashnode_t *this = hm->table[i];
		while (this!=NULL) {
      temp = this;
      this = this->next;
      free(temp);
		}
	}
}


void hashmap_show_structure(hashmap_t *hm) {
	printf("item_count: %d\n", hm-> item_count);
	printf("table_size: %d\n", hm->table_size);
	printf("load_factor: %.4f\n", (double)hm->item_count / (double)hm->table_size);

	for (int i = 0; i < hm->table_size; i++) {
		hashnode_t *temp = hm->table[i];
		printf("%3d :",i);
		while (temp != NULL) {
			printf(" {(%ld) %s : %s}",hashcode(temp->key), temp->key, temp->val);
			temp = temp->next;
		}
		printf("\n");
	}

}

void hashmap_write_items(hashmap_t *hm, FILE *out) {
	for (int i = 0; i < hm->table_size; i++) {
		hashnode_t *temp = hm->table[i];
    if(temp!=NULL){
  		while (temp != NULL) {
  			fprintf(out, "%12s : %s\n", temp->key, temp->val);
  			temp = temp->next;
  		}
    }
	}
}

void hashmap_save(hashmap_t *hm, char *filename) {
	FILE *out = fopen(filename, "w");
	fprintf(out, "%d", hm->table_size);
  fprintf(out, " %d\n", hm->item_count);
	hashmap_write_items(hm, out);
  fclose(out);
}

int hashmap_load(hashmap_t *hm, char *filename) {
	FILE *fh = fopen(filename,"r");
	if (fh == NULL) {
		printf("ERROR: could not open file 'somefile.hm");
		return 0;
	}
	hashmap_free_table(hm);

  int tablesize;
  int itemcount;
  fscanf(fh,"%d",&tablesize);
  fscanf(fh,"%d",&itemcount);

  hashmap_init(hm,tablesize);

  char key[128];
  char val[128];
  char nothing[128];
  while(fscanf(fh,"%s%s%s",key,nothing ,val )!=EOF){
    hashmap_put(hm, key, val);
  }
  fclose(fh);
  return 1;
}

int primeness(int num){
  int half = num/2;
  for(int i=2;i<half+1;i++){
    if(num%i == 0){
        return 0;
    }
  }
  return 1;
}


int next_prime(int num){
  if(primeness(num)==1){
    return num;
  }


  if(num%2!=0){
    num += 2;
  }
  else{
    num += 1;
  }

  while(primeness(num)!=1){
    num+=2;
  }
  return num;
}

void hashmap_expand(hashmap_t *hm){
  hashmap_t old = *hm;
  hashmap_t *oldmap = &old;
  hashmap_init(hm,next_prime(2*(oldmap->table_size)+1));

  for(int i=0;i<oldmap->table_size;i++){
    hashnode_t *temp = oldmap->table[i];
    if(temp!=NULL){
      while(temp!=NULL){
        hashmap_put(hm,temp->key,temp->val);
        temp = temp->next;
      }
    }
  }
  hashmap_free_table(oldmap);
}
