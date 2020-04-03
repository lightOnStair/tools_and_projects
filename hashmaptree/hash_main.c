#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashmap.h"

int main(int argc, char *argv[]){
  int echo = 0;
  if(argc >1 && strcmp("-echo",argv[1])==1){
    echo=1;
  }
  printf("Hashmap Demo\n");
  printf("Commands:\n");
  printf("  hashcode <key>   : prints out the numeric hash code for the given key (does not change the hash map)\n");
  printf("  put <key> <val>  : inserts the given key/val into the hash map, overwrites existing values if present\n");
  printf("  get <key>        : prints the value associated with the given key or NOT FOUND\n");
  printf("  print            : shows contents of the hashmap ordered by how they appear in the table\n");
  printf("  structure        : prints detailed structure of the hash map\n");
  printf("  clear            : reinitializes hash map to be empty with default size\n");
  printf("  save <file>      : writes the contents of the hash map the given file\n");
  printf("  load <file>      : clears the current hash map and loads the one in the given file\n");
  printf("  next_prime <int> : if <int> is prime, prints it, otherwise finds the next prime and prints it\n");
  printf("  expand           : expands memory size of hashmap to reduce its load factor\n");
  printf("  quit             : exit the program\n");

  hashmap_t hm;
  char cmd[128];
  hashmap_init(&hm,HASHMAP_DEFAULT_TABLE_SIZE);

  while(1){
    printf("HM> ");
    int read = fscanf(stdin,"%s",cmd);
    if(read == EOF){
      break;
    }
    if(strcmp("quit",cmd)==0){
      if(echo){
        printf("quit\n");
      }
      break;
    }
    else if(strcmp("hashcode",cmd)==0){
      fscanf(stdin,"%s",cmd);
      long res = hashcode(cmd);
      printf("%ld\n",res);
      if(echo){
        printf("hashcode %ld \n",res);
      }
    }
    else if(strcmp("put",cmd)==0){
      char key[128];
      char val[128];
      fscanf(stdin,"%s",key);
      fscanf(stdin,"%s",val);
      int res = hashmap_put(&hm,key,val);
      if(echo){
        if(res==1){
          printf("%s added\n",key);
        }
        else{
          printf("%s val changed to %s\n",key,val);
        }
      }
    }
    else if(strcmp("get",cmd)==0){
      fscanf(stdin,"%s",cmd);
      char *res = hashmap_get(&hm,cmd);
      if(res!=NULL){
        printf("FOUND: %s\n",res);
      }
      else{
        printf("NOT FOUND\n");
      }

      if(echo){
        printf("get operation\n");
      }
    }
    else if(strcmp("clear",cmd)==0){
      hashmap_free_table(&hm);
      hashmap_init(&hm,5);
    }
    else if(strcmp("print",cmd)==0){
      if(echo){
        printf("print\n");
      }
      hashmap_write_items(&hm,stdout);
    }
    else if(strcmp("structure",cmd)==0){
      if(echo){
        printf("show structure\n");
      }
      hashmap_show_structure(&hm);
    }
    else if(strcmp("save",cmd)==0){
      fscanf(stdin,"%s",cmd);
      if(echo){
        printf("save %s\n",cmd);
      }
      hashmap_save(&hm,cmd);
    }
    else if(strcmp("load",cmd)==0){
      fscanf(stdin,"%s",cmd);
      int res = hashmap_load(&hm,cmd);
      if(echo){
        if(res==1){
          printf("loaded");
        }
        else{
          printf("load failed");
        }
      }
      hashmap_load(&hm,cmd);
    }
    else if(strcmp("next_prime",cmd)==0){
      if(echo){
        printf("next prime");
      }
      int thisprime;
      fscanf(stdin,"%d",&thisprime);
      printf("%d",next_prime(thisprime));
    }
    else if(strcmp("expand",cmd)==0){
      if(echo){
        printf("expand the hashmap\n");
      }
      hashmap_expand(&hm);
    }
    else{
      if(echo){
        printf("%s\n",cmd);
      }
      printf("unknown command %s\n",cmd);
    }
  }
  hashmap_free_table(&hm);
  return 0;
}
