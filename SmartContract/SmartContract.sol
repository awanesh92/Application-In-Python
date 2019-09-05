pragma solidity ^0.5.7;
contract will{
    address owner;
    uint fortune;
    bool isDeceased;
    constructor() public payable{
        owner=msg.sender;
        fortune=msg.value;
        isDeceased=false;
    }
    
    modifier onlyOwner{
        require(msg.sender==owner);
        _;
    }
    modifier mustBeDeceased{
        require(isDeceased==true);
        _;
    }
    
    address payable [] familwallets;
    mapping (address => uint) inheritance;
    
    function setinheritance(address payable wallet,uint inheritamt) public onlyOwner{
        familwallets.push(wallet);
        inheritance[wallet]=inheritamt;
    }
    
    function payout() private mustBeDeceased{
        for(uint i=0;i<familwallets.length;i++)
            familwallets[i].transfer(inheritance[familwallets[i]]);
    }
    
    function deceased() public onlyOwner{
        isDeceased=true;
        payout();
    }
}