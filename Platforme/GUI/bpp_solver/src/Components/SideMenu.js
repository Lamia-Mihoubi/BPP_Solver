import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

import { withStyles } from "@material-ui/core/styles";
import logo from '../pinklogo.png'; // Tell webpack this JS file uses this image
import QueueIcon from '@material-ui/icons/Queue';
import EventNoteIcon from '@material-ui/icons/EventNote';
import AutorenewIcon from '@material-ui/icons/Autorenew';
class SideMenu extends React.Component {
  constructor(props){
        super(props)
        this.state= {
            btnID : 0
        }
  }
    render(){
        const { classes } = this.props;        
      
        return(
                <List component="nav" className={classes.appMenu} disablePadding>
                    <ListItem>
                        <img src={logo} alt="Logo" />
                    </ListItem>
                    
                     <ListItem button className={classes.btn} onClick={()=>{this.props.handler(0)}} >
                    <ListItemIcon>
                        <QueueIcon 
                        style={{ color: '#e898ac' , fontSize: 30 }} 
                        />
                    </ListItemIcon>
                    <ListItemText primary="Créer une Instance" />
                    </ListItem>
                    <ListItem button className={classes.btn} onClick={()=>{this.props.handler(1)}} >
                    <ListItemIcon>
                        <AutorenewIcon
                       style={{ color: '#e898ac' , fontSize: 30 }}  />
                    </ListItemIcon>
                    <ListItemText primary="Générateur aléatoire" />
                    </ListItem>
                    <ListItem button className={classes.btn} onClick={()=>{this.props.handler(2)}} >
                    <ListItemIcon>
                        <EventNoteIcon
                        style={{ color: '#e898ac' , fontSize: 30 }}  />
                    </ListItemIcon>
                    <ListItemText primary="Scholl Benchmark" />
                    </ListItem>
                </List>       
                        
        );
    }
}


const styles = theme => ({
    appMenu: {
      width: '100%',
      height: '100%',
      backgroundColor: '#002845',
    },
    btn :{
        height: '6vw',
    }
  })


export default withStyles(styles)(SideMenu);
