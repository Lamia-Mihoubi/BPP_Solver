import React from "react";
import ChooseMthd from "./ChooseMthd";
import ShowResults from "./ShowResults";
class MainContent1 extends React.Component {
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
    // set a variable list on the state ( for dynamic UI results)
    this.setState({
      display_choosemthd: 0,
      display_showresults: 1,
      solutions: solution,
    });
  }
  handleretour() {
    this.setState({
      display_choosemthd: 1,
      display_showresults: 0,
    });
  }

  render() {
    let content;
    if (this.state.display_choosemthd) {
      content = (
        <div>
          {" "}
          <ChooseMthd
            pagenum={2}
            handleValider={this.handleValider}
          ></ChooseMthd>{" "}
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
    return content;
  }
}

export default MainContent1;
