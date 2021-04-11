/*This program will model a cellular phone network. The system consists of a number of towers (base
stations) and a number of phones. A phone communicates with a single tower -- the tower that is closest
to the phone, within its transmission range. A tower can communicate with any phone that is associated
with that tower, and it may communicate with a specified set of other towers.
 * The file contains the list of functions associated with phoneNode and phone structs. List of functions are:
 * createPhone() - Creates and returns a new phone with the specified ID and location
 * phoneID() - returns the ID associated with the phone
 *phoneLocation() - given a phone, assigns its location to the pointers provided
 *phoneTower()- return the Tower to which phone is currently connected
 * findPhone() - return the phone with matching ID
 * movePhone() -move phone to a new location
 *
 * Akshay Kamalapuram Sridhar 15th November 2020
 */
#include "PhoneTower.h"
#include <stdlib.h>
#include <math.h>
#include <string.h>
struct phone {
    char id[13];  //unique identifier for each struct phone instance
    int x; //x-coordinate
    int y; //y-coordinate
    struct tower *near_tower; //closest tower associated with the phone
};

static struct phoneNode *allphones=NULL; //list of all the phones created

//Creates and returns a new phone with the specified ID and location. Input arguments provided are the id, x-coordinate and y-coordinate
Phone createPhone(const char *id, int x, int y) {
    if (x<0 || y<0) return NULL; //if the coordinates are negative, the phone won't be created

    //finding the nearest tower
    struct towerNode *t=allTowers();
    struct tower *t_dum=NULL;
    double dist=10000.0; //used to store the distance of the nearest tower to the phone
    double dist_dum=0; //used for comparing the current distance with previous value
    double dist_1=0; //contains the squared value of the distance
    int square_dist=0; //used to calculate the squared value of the distance
    int xaddr=0;
    int yaddr=0;
    while (t) { //traverses the list of all the towers to find the nearest one
        towerLocation(t->tower,&xaddr,&yaddr);  //given a Tower, assigns its location to the the pointers provided
        square_dist=((x-xaddr)*(x-xaddr)) + ((y-yaddr)*(y-yaddr)); //calculate the distance
        dist_1=(double)(square_dist);
        dist_dum=sqrt(dist_1);
        if (dist>dist_dum) { //compares the current to previous distance
            dist=dist_dum;
            t_dum=t->tower; //assigns the tower associated with the distance to the pointer
        }
        if (dist==dist_dum){ //if distances are equal,the tower assigned to the phone will be the one which is alphabetically first
            if (strcmp(towerID(t->tower),towerID(t_dum))<0) t_dum=t->tower;
        }
        t=t->next;
    }
    struct phoneNode *newnode=malloc(sizeof(struct phoneNode));  //creates a new phoneNode
    struct phone *newphone=malloc(sizeof(struct phone)); //creates a new phone
    strcpy(newphone->id,id); //copying contents to new phone
    newphone->x=x;
    newphone->y=y;
    newphone->near_tower=NULL;
    if (dist<=3.0){ //assigning the closest tower to the phone
        newphone->near_tower=t_dum;
    }
    else newphone->near_tower=nullTower(); //if no tower is within the range of the phone nulltower() will be assigned
    newnode->phone=newphone;
    //adding the phone to the list of phones in ascending order
    struct phoneNode *p=allphones;
    struct phoneNode *prev=NULL;
    while (p && (strcmp(p->phone->id,newphone->id)<0)){
        prev=p;
        p=p->next;
    }
    newnode->next=p;
    if (prev) prev->next=newnode;
    else allphones=newnode;

    //adding phone to tower's list of phones
    addPhone(newphone->near_tower,newphone);
    return newphone; //returns the phone created
}

//returns the ID associated with the phone provided as an argument
const char * phoneID(Phone p){
    return p->id;
}

//given a phone, assigns its location to the pointers provided
void phoneLocation(Phone p, int *xaddr, int *yaddr){
    if (xaddr) *xaddr=p->x;
    if (yaddr) *yaddr=p->y;
}

//given a Phone, return the Tower to which it is currently connected
Tower phoneTower(Phone p){
    return p->near_tower;
}

//return the phone with matching ID (or NULL if not found)
Phone findPhone(const char *id){
    struct phoneNode *p=allphones; //pointer to the list of phones
    if (p==NULL) return NULL; //if no phone is created return NULL
    while (p) {
        if (strcmp(id,p->phone->id)==0) { //checks for the phone with the matching id
            return p->phone; //returns the matched phone
        }
        p=p->next;
    }
    return NULL; //returns NULL if no phone is found in the list
}

//move existing phone to a new location. The phone and the new location are provided as input arguments
void movePhone(Phone p, int newx, int newy){
  p->x=newx; //changing the coordinates of the phone
  p->y=newy;
  removePhone(p->near_tower,p); //removes a phone ,provided as an argument, from the tower, provided as the argument
  //finding the nearest tower
    struct towerNode *t=allTowers();
    //struct phoneNode *m;
    double dist=10000.0;//used to store the distance of the nearest tower to the phone
    double dist_dum=0;//used for comparing the current distance with previous value
    double dist_1=0;//contains the squared value of the distance
    int square_dist=0;//used to calculate the squared value of the distance
    int xaddr=0;
    int yaddr=0;
    struct tower *t_dum=NULL;
    while (t) { //traverses the list of all the towers to find the nearest one
        towerLocation(t->tower,&xaddr,&yaddr); //given a Tower, assigns its location to the the pointers provided
        square_dist=((newx-xaddr)*(newx-xaddr)) + ((newy-yaddr)*(newy-yaddr)); //calculate the distance
        dist_1=(double)(square_dist);
        dist_dum=sqrt(dist_1);
        if (dist>dist_dum) { //compares the current to previous distance
            dist=dist_dum;
            t_dum=t->tower; //assigns the tower associated with the distance to the pointer
        }
        t=t->next;
    }
    if (dist<=3.0){ //assigning the closest tower to the phone
        p->near_tower=t_dum;
    }
    else p->near_tower=nullTower();  //if no tower is within the range of the phone nulltower() will be assigned
    addPhone(p->near_tower,p); //adding phone to tower's list of phones
}