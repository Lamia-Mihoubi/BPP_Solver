import React from "react";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import ChooseMthd from "./ChooseMthd";
import { withStyles } from "@material-ui/core/styles";
import ShowResults from "./ShowResults";


class SchollPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      display_choosemthd: 1,
      display_showresults: 0,
      solutions: "",
    };
    this.handleValider = this.handleValider.bind(this);
    this.handleretour = this.handleretour.bind(this);
  }

  handleValider(solution) {
    this.setState({
      solutions: solution,
      display_choosemthd: 0,
      display_showresults: 1,
    });
  }
  handleretour() {
    this.setState({
      display_choosemthd: 1,
      display_showresults: 0,
    });
  }

  render() {
    const classes = this.props;
    let content;
    
    if (this.state.display_choosemthd) {
      content = (
        <div>
          
          <ChooseMthd
            pagenum={3}
            handleValider={this.handleValider}
          ></ChooseMthd>
        </div>
      );
    }
    if (this.state.display_showresults) {
      // when backend is done change to solutions={this.state.solutions}
      content = (
        <ShowResults
          n="5"
          c="10"
          sol_opt="1"
          solutions={this.state.solutions}
          handleretour={this.handleretour}
        ></ShowResults>
      );
    }
    return (
      <Container>
       
        
        <div className={classes.empty}></div>
        {content}
      </Container>
    );
  }
}
const styles = (theme) => ({
  root: {
    //backgroundColor: '#020F59',
  },
  drawerPaper: {},
  pagetitle: {
    margin: theme.spacing(1),
  },
  empty: {
    height: "9vw",
  },
});

export default withStyles(styles)(SchollPage);
