import React, { Fragment } from 'react';
import {Container,TextField,Button,Grid,Box} from '@material-ui/core'
import { spacing } from '@material-ui/system';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { makeStyles } from '@material-ui/core/styles';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { FixedSizeList } from 'react-window';
import data from '../data/instance.json'
class FormNC extends React.Component
{   const(props)
    {
        
        this.objects=props.objects
    }
    generateclick(){
        //send request first
        console.log("clicked")
        
    }
    renderRow() {
       return( data.map(d=>(
           <ListItem>{d}</ListItem>
       ) )
       )
    }
render()
{
    return(
        <React.Fragment>
        
        <Box m={2} p={2}>
            <form>
                <Grid container spacing={3}>
                <Grid item xs={10} sm={3}>
                    <TextField  variant="outlined"  label="Nombre d'objets " size="small" />
                </Grid>
                <Grid item xs={10} sm={3}>
                    <TextField variant="outlined" label="Capacité des boites " size="small" />
                </Grid>
                
                <Grid item xs={12}>
                         <Button variant="contained" color="primary"  onClick={this.generateclick}>
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
         <FixedSizeList height={200} width={200} itemSize={46} itemCount={1}>
        {this.renderRow}
         </FixedSizeList>
         </ExpansionPanelDetails>
       </ExpansionPanel> 
        </Box>
    
       </React.Fragment>


    )
}
}
export default FormNC