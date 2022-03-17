// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FakeSyrup {
    // Whether a limit is set for users
    bool public userLimit;
    // The pool limit (0 if none)
    uint256 public poolLimitPerUser;
    mapping(address => uint256) public userInfo;

    function deposit(uint256 _amount) public {
        userInfo[msg.sender] = _amount;
    }
}
