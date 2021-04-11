/*This program will model a cellular phone network. The system consists of a number of towers (base
stations) and a number of phones. A phone communicates with a single tower -- the tower that is closest
to the phone, within its transmission range. A tower can communicate with any phone that is associated
with that tower, and it may communicate with a specified set of other towers.
 * The file contains the list of functions associated with towerNode and tower structs. List of functions are:
 *
 *createTower() - Creates and returns a new Tower with the specified ID and location
 * towerID() - returns the ID associated with the tower
 * towerLocation() - //given a Tower, assigns its location to the the pointers provided
 * nullTower() - Returns the null tower
 * alltowers() - Returns the list of all towers
 * findTower() - return the Tower with matching ID
 * addConnection() - create a connection between two Towers
 * towerNeighbors() - return a list of Towers connected to that Tower
 * addPhone() - adds the phone to the tower's list of phones
 * removePhone() - removes a phone ,provided as an argument, from the tower, provided as the argument
 * towerPhones() - given a Tower, return a list of Phones connected to that Tower
 * routeInternal() - Uses "depth-first" search algorithm to find a route from starting tower T1 to a receiving phone T2, as requested by tower prev. It returns the route to reach from t1 to t2
 * routeCall() - //routes a call between two phones, start to end
 *
 * Akshay Kamalapuram Sridhar 15th November 2020
 */
#include <stdlib.h>
#include "PhoneTower.h"
#include <string.h>
#include <stdio.h>

struct tower{
    char id[13]; //unique identifier for each struct tower instance
    int x; //x-coordinate
    int y; //y-coordinate
    struct towerNode *neighbour; //list of tower neighbors
    struct phoneNode *near_phones; //list of phones connected to the tower
};

static struct towerNode *alltowers=NULL; //list of all the towers created

static struct tower nulltower={"None",0,0,NULL,NULL}; //creation of nulltower instance
static struct tower *null1=&nulltower; //Pointer to the null tower

//Creates and returns a new Tower with the specified ID and location. Input arguments provided are the id, x-coordinate and y-coordinate
Tower createTower(const char *id, int x, int y){
    if (x<0 || y<0) return NULL; //if the coordinates are negative, the tower won't be created
    struct towerNode *newnode=malloc(sizeof(struct towerNode)); //creates a new towerNode
    struct tower *newtower=malloc(sizeof(struct tower)); //creates a new tower
    strcpy(newtower->id,id); //copying inputs to the tower fields
    newtower->x=x;
    newtower->y=y;
    newtower->near_phones=NULL; //assigning the lists in the tower to NULL
    newtower->neighbour=NULL;
    newnode->tower=newtower; //copying contents of tower to the newnode
    newnode->next=NULL;
    struct towerNode *p=alltowers;
    struct towerNode *prev=NULL;
    while (p && (strcmp(p->tower->id,newtower->id)<0)) { //inserting the newnode in the list in ascending order
        prev=p;
        p=p->next;
    }
    newnode->next=p;
    if (prev) prev->next=newnode;
    else alltowers=newnode;
    return newtower; //returns the tower created
}

//returns the ID associated with the tower provided as an argument
const char * towerID(Tower t) {
    return t->id;
}

//given a Tower, assigns its location to the the pointers provided
void towerLocation(Tower t, int *xaddr, int *yaddr){
    int x1=t->x; //assigns the tower's location coordinates to the variable
    int y1=t->y;
    if (xaddr) *xaddr=x1; //if not NULL, assign the pointer with the tower's coordinates
    if (yaddr) *yaddr=y1;
}

//Returns the pointer to the null tower
Tower nullTower() {
    return null1;
}

//returns the list of all towers
TowerNode allTowers(){
    return alltowers;
}

//return the Tower with matching ID (or NULL if not found)
Tower findTower(const char *id){
    struct towerNode *p=alltowers; //pointer to the list of towers
    if (p==NULL) return NULL; //if no tower is created return NULL
    while (p) {
          if (strcmp(id,p->tower->id)==0) { //checks for the tower with the matching id
               return p->tower; //returns the matched tower
            }
         p=p->next;
    }
    return NULL; //returns NULL if no tower is found
}

//create a connection between two Towers
//t2 will be added to t1's neighbor list
//t1 will be added to t2's neighbor list
//t1 and t2 are the arguments
void addConnection(Tower t1, Tower t2) {
    int count = 0; //counter variable to check if the towers are already connected i.e there in each other's neighbor list
    struct towerNode *p = t1->neighbour; //assigns pointer to the neighbor list of t1

    while (p) {
        if (strcmp(p->tower->id, t2->id)==0) { //checks if t2 already exists in t1's neighbor list using their id
            ++count;
            break;
        }
        p = p->next;
    }
    if (count == 0) { // if towers aren't connected already

        //Below is the code for adding t2 to t1's neighbor list
        struct towerNode *newnode = malloc(sizeof(struct towerNode)); //creates a new towerNode
        newnode->tower = t2; //copying contents of tower to the newnode
        newnode->next = NULL;
        p = t1->neighbour; //re-assigns pointer to the neighbor list of t1
        struct towerNode *prev = NULL;
        while (p && (strcmp(p->tower->id, t2->id) < 0)) { //inserting the newnode in the list in ascending order
            prev = p;
            p = p->next;
        }
        newnode->next = p;
        if (prev) prev->next = newnode;
        else t1->neighbour = newnode;

        //Below is the code for adding t1 to t2's neighbor list
        struct towerNode *newnode1 = malloc(sizeof(struct towerNode)); //creates a new towerNode
        newnode1->tower = t1;//copying contents of tower to the newnode
        newnode1->next = NULL;
        struct towerNode *prev1 = NULL;
        struct towerNode *p1 = t2->neighbour; //assigns pointer to the neighbor list of t1
        while (p1 && (strcmp(p1->tower->id, t1->id) < 0)) { //inserting newnode1 in the list in ascending order
            prev1 = p1;
            p1 = p1->next;
        }
        newnode1->next = p1;
        if (prev1) prev1->next = newnode1;
        else t2->neighbour = newnode1;
    }
}

//given a Tower, return a list of Towers connected to that Tower
TowerNode towerNeighbors(Tower t){
    return t->neighbour;
}

//adds the phone to the tower's list of phones. Both the phone and the tower to which the phone must be connected to, are provided as arguments
void addPhone(Tower t, Phone p){
    struct phoneNode *phone1=t->near_phones; //assigns pointer to the list of phones of t
    int count=0; //counter variable to check if phone is already connected to the tower
    while (phone1){
        if (strcmp(phoneID(phone1->phone),phoneID(p))==0) { //checks if the phone already exists in t1's list using the phone id's
            ++count;
            break;
        }
        phone1=phone1->next;
    }
    if (count==0) { // if phone isn't connected already
        //Below is the code for adding p to t1's phone list
        phone1=t->near_phones; //re-assigns pointer to the list of phones
        struct phoneNode *newnode=malloc(sizeof(struct phoneNode));  //creates a new phoneNode
        newnode->phone=p; //copying contents of phone to the newnode
        newnode->next=NULL;
        struct phoneNode *prev=NULL;
        while (phone1 && (strcmp(phoneID(phone1->phone),phoneID(p))<0)){ //inserting the newnode in the list in ascending order
            prev=phone1;
            phone1=phone1->next;
        }
        newnode->next=phone1;
        if (prev) prev->next=newnode;
        else t->near_phones=newnode;
    }

}

//removes a phone ,provided as an argument, from the tower, provided as the argument
void removePhone(Tower t, Phone p) {
    struct phoneNode *phone1 = t->near_phones; //assigns pointer to the list of phones of t
    struct phoneNode *prev = NULL;
    while (phone1 && (strcmp(phoneID(phone1->phone), phoneID(p))<0)) { //traverses along the list till it finds the phone
        prev = phone1;
        phone1 = phone1->next;
    }
    if (phone1) {  //changes the next field of the pointers to remove the phone
        if (prev) prev->next = phone1->next;
        else t->near_phones = phone1->next;
    }
}

//given a Tower, return a list of Phones connected to that Tower
PhoneNode towerPhones(Tower t){
    return t->near_phones;
}

//The routeInternal implementation uses the
//"depth-first" search algorithm to find a route from starting tower T1 to a receiving phone T2, as requested by tower prev. It returns the route to reach from t1 to t2
TowerNode routeInternal(Tower t1,Tower t2, Tower prev){
    struct towerNode *list1=t1->neighbour; //assigns pointer to the neighbor list of t1
    struct towerNode *list=list1; //assigns pointer to list1 pointer
    if (t1==t2){ //if the start tower is equal to the end tower, a towerNode is created to add the tower to that node. The node is then returned
        struct towerNode *newnode=malloc(sizeof(struct towerNode));
        newnode->tower=t1; //copying contents of tower to the newnode
        newnode->next=NULL;
        return newnode;
    }
    while(list){ //traverses the list of neighbors of the tower
        if ((list->tower==prev) || (list->tower==nullTower())) {} //if the neighbor tower is same as prev then the iteration doesn't do anything except go to the next neighbor in the list
        else {
            struct towerNode *r=routeInternal(list->tower,t2,t1); //creates a recursion by doing routeInternal for neighbor tower's neighbor list in order to try to see if any of it's neighbors is t2
            if (r!=NULL) { // if r has a value apart from NULL
                struct towerNode *newnode = malloc(sizeof(struct towerNode)); //creates a new towerNode
                newnode->tower = t1; //copying contents of tower to the newnode
                newnode->next = NULL;
                newnode->next=r; //prepends the node to r
                return newnode; //returns the list of towers used for routing (in order)
            }
        }
        list=list->next;
    }
   return NULL; //if no route can be made returns NULL
}

//routes a call between two phones, start to end
//returns a list of Towers required to connect the call, in routing order
TowerNode routeCall(Phone start, Phone end){
    struct tower *t1=phoneTower(start); //assigns the pointer to the nearest tower associated with the start phone
    struct tower *t2=phoneTower(end); //assigns the pointer to the nearest tower associated with the end phone
    struct towerNode *r= routeInternal(t1,t2, NULL); //assigns r with the list of towers required to connect the call in routing order
    return r; //returns the list of towers
}


