## Upcoming 2.0.0<a name="2.0.0"></a> (2022-11-28)

### Bug Fixes

- **default_lighting:** make attributes optional ([30f55fe](https://github.com/balandbal/urdf2mjcf/commit/30f55fe4accb16ab1a713cdc26ddce3666dfc611))

### Build

- remove irrelevant pytest dependency ([75ba99a](https://github.com/balandbal/urdf2mjcf/commit/75ba99abc46e7fa4329be1d4273a11702fe0de1e))

### Chore

- **roslaunch:** extend with ground and lighting ([4af0801](https://github.com/balandbal/urdf2mjcf/commit/4af0801a264502bf448c7265fcadfc54a23ca427))

### Code Refactoring

- **core:** move full_pipeline into module app ([965f523](https://github.com/balandbal/urdf2mjcf/commit/965f523183373921fe2339331f41f5e9440f6c94))

### Docs

- **changelog:** add template and generation info ([0085b0e](https://github.com/balandbal/urdf2mjcf/commit/0085b0e89cd6742d67d6aa9c7fa8f2222bbcefce))

### Features

- **app:** integrate default ground and lighting ([ce78d85](https://github.com/balandbal/urdf2mjcf/commit/ce78d85a9c6acc310ece3ab98e1fe3c8dcf2e7b9))
- **cli:** expose default ground and lighting ([6d420e5](https://github.com/balandbal/urdf2mjcf/commit/6d420e59e70ded66a1bdae6018ffd767042e7374))
- **rosnode:** expose all of the urdf2mjcf args ([51ccaff](https://github.com/balandbal/urdf2mjcf/commit/51ccaff2f418e68322795b77058e6e8b2dc216e5))
- **rosnode:** expose default ground and lighting ([626c950](https://github.com/balandbal/urdf2mjcf/commit/626c950acf2c7fb8e34693e396f6887254f2a419))
- **rosnode:** make get_param default required ([5ec0f17](https://github.com/balandbal/urdf2mjcf/commit/5ec0f1747bceaafa427cf86074f357b56f5dbf8d))
- add postprocess function to add ground plane ([32cc9a0](https://github.com/balandbal/urdf2mjcf/commit/32cc9a0b777dfd25d567d1b2c841b4932239b483))
- add postprocess function to add lighting ([45b9801](https://github.com/balandbal/urdf2mjcf/commit/45b98012ab298b7e3c5e33abe2e1dd44ab84e1ca))

### Style

- **roslaunch:** harmonize quotation marks ([d11f3e7](https://github.com/balandbal/urdf2mjcf/commit/d11f3e7507cd807f436e0ad96a1edde9d7558f29))

### Tests

- ensure imports work within the test folder ([6bfb1bf](https://github.com/balandbal/urdf2mjcf/commit/6bfb1bff91fabe5fa0f2ba8ddc0756b78e40e071))
- expose tests to catkin ([49e231a](https://github.com/balandbal/urdf2mjcf/commit/49e231a69c889badc8bc2cd9a074650c3e8e4d6c))
- make ROS URI test more general ([37da775](https://github.com/balandbal/urdf2mjcf/commit/37da77556695ebaa285a0372bd09d1178b5cd028))
- make test assertion more descriptive ([6300f3f](https://github.com/balandbal/urdf2mjcf/commit/6300f3f6a029d5b2d1b8e2bda029f507718fb064))
- remove asset elements from parse tests ([0be5ac9](https://github.com/balandbal/urdf2mjcf/commit/0be5ac9b2da97c7247b14e9b4075e5ae30576231))
