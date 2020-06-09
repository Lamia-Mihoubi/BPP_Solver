import React,{Component } from 'react';
import Container from '@material-ui/core/Container'
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import { withStyles } from '@material-ui/core/styles';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import FormLabel from '@material-ui/core/FormLabel';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import { render } from '@testing-library/react';
import { MDBInput } from 'mdbreact';
import './inputPage.css';
import { MDBContainer, MDBInputGroup, MDBBtn } from "mdbreact";
import { MDBTable, MDBTableBody, MDBTableHead } from 'mdbreact';


class Instance extends Component{
    state = {
        value: 0
      }
    
      decrease = () => {
          if(this.state.value>0){
            this.setState({ value: this.state.value - 1 });
          }
        
      }
    
      increase = () => {
        this.setState({ value: this.state.value + 1 });
      }
      nbitems={
          value:0
      }
      capacite={
          value:0
      }
      ajouterItem=()=>{
          console.log("pfff")
          const nbreitems=document.querySelector('.NBartics')
          console.log(nbreitems.value)
          this.capacite.value=document.querySelector('.cap').value
          if(parseInt(this.nbitems.value)<parseInt(nbreitems.value)){
                const a =document.querySelector('#idd')
                console.log(this.capacite.value)
                console.log(typeof a.value)
              if(parseInt(this.capacite.value) >= parseInt(a.value)){
                console.log(a.value)
                this.nbitems.value=this.nbitems.value + 1
                // Find a <table> element with id="myTable":
                let table = document.querySelector('.table1');
    
                // Create an empty <tr> element and add it to the 1st position of the table:
                let row = table.insertRow(-1);
    
                // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
                let cell1 = row.insertCell(0);
                let cell2 = row.insertCell(1);
    
                // Add some text to the new cells:
                cell1.innerHTML = this.nbitems.value; 
                cell2.innerHTML = a.value
                a.value=""
                a.defaultValue=""
                console.log(a)
              }
            
            }
            if(this.nbitems.value==nbreitems.value){
                let table = document.querySelector('.table1');
                document.querySelector('#btn-add').disabled=true
                let objects=[]
                for (let i=1;i<table.rows.length;i++){
                    objects[i-1]=table.rows[i].cells[1].innerHTML
                }
                const problem={
                    nb_articles:this.nbitems.value,
                    capacite:this.capacite.value,
                    objets:objects
                }
                console.log(JSON.stringify(problem))
            }
      }
    render(){
        return(
            
            <Container className="container-style">
                <Card className="card-style"/*className={classes.root}*/>
                    <CardHeader 
                        title="Entrez les paramètres de l'instance"
                    />
                    <CardContent>
                        <MDBContainer>
                            <MDBInputGroup className="NBartics"
                                material
                                containerClassName="mb-1 mt-0"
                                hint="Nombre d'articles"
                                />
                            <MDBInputGroup className="cap"
                                material
                                containerClassName="mb-1 mt-0"
                                hint="Capacité"
                                />
                            <MDBInputGroup className="ajouter_art"
                                id="idd"
                                material
                                containerClassName="mb-1 mt-0"
                                hint="Ajouter Article"
                                append={
                                    <MDBBtn 
                                    id="btn-add"
                                    color="teal lighten-2"
                                    className="m-0 px-3 py-2 z-depth-0"
                                    onClick={this.ajouterItem}
                                    >
                                    +
                                    </MDBBtn>
                                }
                                />
                        </MDBContainer>
                        <MDBTable className="table1">
                            <MDBTableHead>
                                <tr>
                                <th>ID</th>
                                <th>Poids</th>
                                </tr>
                            </MDBTableHead>
                            
                        </MDBTable>
                    </CardContent>
                </Card>
            </Container>
            
        ) 
    }
}

export default Instance;