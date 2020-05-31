import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/Inbox';
import DraftsIcon from '@material-ui/icons/Drafts';
import { withStyles } from "@material-ui/core/styles";
import logo from '../4.png'; // Tell webpack this JS file uses this image
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
                    
                     <ListItem button  onClick={()=>{this.props.handler(0)}} >
                    <ListItemIcon>
                        <QueueIcon />
                    </ListItemIcon>
                    <ListItemText primary="Create Instance" />
                    </ListItem>
                    <ListItem button  onClick={()=>{this.props.handler(1)}} >
                    <ListItemIcon>
                        <AutorenewIcon />
                    </ListItemIcon>
                    <ListItemText primary="Use Samples" />
                    </ListItem>
                    <ListItem button  onClick={()=>{this.props.handler(2)}} >
                    <ListItemIcon>
                        <EventNoteIcon />
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
    }
  })


export default withStyles(styles)(SideMenu);
