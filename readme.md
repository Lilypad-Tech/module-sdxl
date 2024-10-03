# SDXL Turbo Pipeline: A Lightweight Module for Lilypad

This README provides instructions for running the SDXL Turbo Pipeline module on the Lilypad network using Docker and Lilypad CLI.

## Prerequisites

- Lilypad CLI installed (for Lilypad network runs)

If you would like to run this Lilypad module locally using the Lilypad localnet
- Docker installed on your system
- GPU

## Running on Lilypad Network

### Using Lilypad LocalNet

To run on the local development network:

```
go run . run --network dev github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53d7cabab1927bb403f02fd2a --web3-private-key <admin_key> -i prompt="your prompt here"
```

Replace `<admin_key>` with the admin key found in `hardhat/utils/accounts.ts`.

Example:
```
go run . run --network dev github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53k7cabab1927bb403f02fd2a --web3-private-key <admin_key> -i prompt="a spaceship parked on mountain"
```

### Using Lilypad Main Network

To run on the main Lilypad network:

```
lilypad run github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53d7cabab1927bb403f02fd2a -i prompt="your prompt here"
```

Example:
```
lilypad run github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53d7cabab1927bb403f02fd2a -i prompt="a spaceship parked on mountain"
```

## Notes

- Ensure you have the necessary permissions and resources to run Docker containers with GPU support.
- The module version (`ae17e969cadab1c53d7cabab1927bb403f02fd2a`) may be updated. Check for the latest version before running.
- Adjust port mappings and volume mounts as needed for your specific setup.
