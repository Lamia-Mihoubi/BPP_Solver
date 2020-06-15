import React,{Component } from 'react';
import { Container, TextField, Button, Grid, Box } from "@material-ui/core";
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import { withStyles } from '@material-ui/core/styles';
import './inputPage.css';
import { MDBContainer, MDBInputGroup, MDBBtn } from "mdbreact";
import { MDBTable, MDBTableBody, MDBTableHead } from 'mdbreact';
import { spacing } from "@material-ui/system";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import Divider from '@material-ui/core/Divider';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

class Instance extends Component{
    state = {
        value: 0
      }
      constructor(props) {
        super(props);
        this.state = {
          n: 10,
          c: 10,
        open: false,} 
          this.ajouterItem=this.ajouterItem.bind(this)
          this.handleChange1 = this.handleChange1.bind(this);
          this.handleChange2 = this.handleChange2.bind(this);
          this.handleClose = this.handleClose.bind(this);
        }
        handleClose(){
          this.setState({
            open:false,
          })
        }
        handleChange1(event) {
          this.setState({ c: event.target.value });
        }
        handleChange2(event) {
          this.setState({ n: event.target.value });
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
      ajouterItem=()=>{
      
       
          
          
          //this.capacite.value=document.querySelector('.cap').value
          if(parseInt(this.state.n)>parseInt(this.nbitems.value)){
                const a =document.querySelector('#idd')
              if(parseInt(this.state.c) >= parseInt(a.value)){
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
              else {
                this.setState({
                  open: true,
                })
              }
            
            }
            if(this.state.n==this.nbitems.value){
                let table = document.querySelector('.table1');
                document.querySelector('#btn-add').disabled=true
                let objects=[]
                for (let i=1;i<table.rows.length;i++){
                    objects[i-1]=table.rows[i].cells[1].innerHTML
                }
                const problem={
                    nb_articles:this.state.n,
                    capacite:this.state.c,
                    objets:objects
                }
                this.props.sendpb(this.state.n,this.state.c,objects);
                console.log(JSON.stringify(problem))
            }
      }
    render(){
        const { classes } = this.props; 
        return(
            
            <Container  width={1} /*className={classes.root}*/>
              <Typography variant="h3" className={classes.pagetitle} gutterBottom>
               Construire votre propre Instance
              </Typography>
                <Card width={1} className={classes.root}>
                    <CardHeader 
                        title="Entrez les paramètres de l'instance"
                    />

                    <CardContent>
                    <Grid container spacing={3} m={5}>
                                      <Grid item xs={10} sm={3}>
                                        <TextField
                                          required
                                          variant="outlined"
                                          type="number"
                                          label="Nombre d'objets "
                                          size="small"
                                          value={this.state.n}
                                          onChange={this.handleChange2}
                                          InputProps={{ inputProps: { min: 0, max: 10 } }}
                                        />
                                      </Grid>
                                      <Grid item xs={10} sm={3}>
                                        <TextField
                                          
                                          required
                                          variant="outlined"
                                          type="number"
                                          label="Capacité des boites "
                                          size="small"
                                          value={this.state.c}
                                          onChange={this.handleChange1}
                                          InputProps={{ inputProps: { min: 0, max: 10 } }}
                                        />
                                      </Grid>
                                </Grid>
                                <br></br>
                                <Divider variant="middle" />
                                <br></br>
                                <div >
                                <p className={classes.ajouter}>
                                        Ajouter un article
                                </p>
                                </div>
                                
                   <MDBContainer m={3}>
                            <MDBInputGroup 
                                id="idd"
                                material
                                containerClassName="mb-1 mt-0"
                                hint="Poids de l'article"
                                append={
                                    <MDBBtn 
                                    id="btn-add"
                                    color="pink lighten-3"
                                    className="m-0 px-3 py-2 z-depth-0"
                                    onClick={this.ajouterItem}
                                    >
                                    +
                                    </MDBBtn>
                                }
                                />
                        </MDBContainer>
                        <br/>
                        <Dialog
                          open={this.state.open}
                          aria-labelledby="alert-dialog-title"
                          aria-describedby="alert-dialog-description"
                        >
                          <DialogTitle id="alert-dialog-title">{"Violation des contraintes du Bin Packing"}</DialogTitle>
                              <DialogContent>
                                <DialogContentText id="alert-dialog-description">
                                  Veuillez introduire un poids valide. 
                                  Le poids d'un objet ne doit jamais dépasser la capacité de la boîte. 
                                </DialogContentText>
                              </DialogContent>
                              <DialogActions>
                                <Button onClick={this.handleClose} color="primary">
                                  OK
                                </Button> 
                                </DialogActions>
                        </Dialog>
                        <ExpansionPanel>
                                    <ExpansionPanelSummary
                                      expandIcon={<ExpandMoreIcon />}
                                      aria-controls="panel1a-content"
                                      id="panel1a-header"
                                    >
                                      Instance générée
                                    </ExpansionPanelSummary>
                                    <ExpansionPanelDetails>
                                    <MDBTable className="table1">
                            <MDBTableHead>
                                <tr>
                                <th>ID</th>
                                <th>Poids</th>
                                </tr>
                            </MDBTableHead>
                            </MDBTable>
                                    </ExpansionPanelDetails>
                                  </ExpansionPanel>

                    </CardContent>
                </Card>
            </Container>
            
        ) 
    }
}

const styles = theme => ({
    root: {
        
        margin: theme.spacing(3),
        width: "67vw",
        marginLeft : "1cm"

      },
    ajouter:
    {
        color: "#6E6F74", 
        fontSize: "19px",
         fontFamily: 'Arial',
         fontWeight: "bold",
         paddingBottom: "10px",
    }

})  
export default withStyles(styles)(Instance);
