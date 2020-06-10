import React, { Fragment } from 'react';
import {Container,TextField,Button,Grid,Box} from '@material-ui/core'
import { spacing } from '@material-ui/system';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import ListItem from '@material-ui/core/ListItem';
import List from '@material-ui/core/List'

import data from '../data/instance.json'
class FormNC extends React.Component
{   constructor(props)
    {  super(props);
        this.state = {
         n:0,
         c:1,
         objects:[0,12,23]
        };  
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange1 = this.handleChange1.bind(this);
        this.handleChange2 = this.handleChange2.bind(this);
     }
 

    handleChange1(event)
     {    this.setState({c: event.target.value}); 
     }
     handleChange2(event)
     {    this.setState({n: event.target.value}); 
     }
    async handleSubmit(event) {
       //c'est la win nebe3tou la rqt
        //alert('Le n a été soumis : ' + this.state.n);
        event.preventDefault();
        var data = {
            "n": this.state.n,
            "c": this.state.c
         }
         
         const response = await fetch("/random", {
            method: "POST",
            headers: { 'Accept': 'application/json','Content-Type': 'application/json',},
            body:  JSON.stringify(data)
         })
         const res = await response.json();
         
         this.setState({objects:res})  ;
         this.props.sendpb(this.state.n,this.state.c, res);
         alert(this.state.objects);
      }
render()
{
    
    return(
        <React.Fragment>
        
        <Box m={2} p={2}>
            <form onSubmit={this.handleSubmit} >
                <Grid container spacing={3}>
                <Grid item xs={10} sm={3}>
                    <TextField  variant="outlined"  label="Nombre d'objets " size="small" value={this.state.n} onChange={this.handleChange2}/>
                </Grid>
                <Grid item xs={10} sm={3}>
                    <TextField variant="outlined"  label="Capacité des boites " size="small" value={this.state.c} onChange={this.handleChange1} />
                </Grid>
                
                <Grid item xs={12}>
                         <Button variant="contained" color="primary" type="submit" >
                    Générer
                </Button>
                </Grid>
                
                </Grid>
               
               
            </form>
            <br></br>
            <ExpansionPanel >
         <ExpansionPanelSummary
           expandIcon={<ExpandMoreIcon />}
           aria-controls="panel1a-content"
           id="panel1a-header" >
          Instance générée
         </ExpansionPanelSummary>
         <ExpansionPanelDetails>
         <List height={200} width={200} itemSize={46} >
        {this.state.objects.map( (d) => { 
            return(
           <ListItem>{d}</ListItem>
            ) })}
         </List>
         </ExpansionPanelDetails>
       </ExpansionPanel> 
        </Box>
    
       </React.Fragment>


    )
}
}
export default FormNC