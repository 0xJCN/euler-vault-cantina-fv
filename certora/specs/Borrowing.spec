import "./Base.spec";

using ESynthHarness as ERC20a; // used for violated run
//using ESynthHarnessFixed as ERC20a; // used for verified run

methods {
    // dispatch and use MockFlashBorrow if more detailed implementation is required
    function _.onFlashLoan(bytes) external => NONDET;
}

// borrowed asset is ESynth, therefore controller is a Synthetic Vault
rule transferBorrowedAssets(env e, address receiver) {
    require receiver != 0;
    require e.msg.sender != 0;
    require e.msg.sender != evc;
    require evc.areChecksInProgress(e) == false;
    require vaultIsOnlyControllerExt(e, e.msg.sender, currentContract);
    require ERC20a.getReentrancyGuardExt(e) == false;

    address asset = getUnderlyingAssetExt(e);
    uint256 balance = ERC20a.balanceOf(e, e.msg.sender);

    require asset == ERC20a;
    require isCollateralEnabledExt(e, e.msg.sender, ERC20a) == false;

    require balance > 0;
    require balance + ERC20a.balanceOf(e, receiver) < max_uint256;

    uint256 collateralValue;
    uint256 liabilityValue;

    (collateralValue, liabilityValue) = calculateLiquidityExt(e, e.msg.sender);
    require collateralValue > 0;
    require liabilityValue > 0;

    ERC20a.transfer@withrevert(e, receiver, balance);

    assert !lastReverted;
}

// used to test running time
//use builtin rule sanity;
