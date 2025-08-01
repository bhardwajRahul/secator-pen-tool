# Changelog

## [0.16.5](https://github.com/freelabz/secator/compare/v0.16.4...v0.16.5) (2025-06-25)


### Bug Fixes

* **celery:** pass mongodb uuids when enabled ([#701](https://github.com/freelabz/secator/issues/701)) ([64b43e8](https://github.com/freelabz/secator/commit/64b43e88659c963a0c526829a2f72ee75348edef))
* **ci:** add apt update in ci ([261d1e8](https://github.com/freelabz/secator/commit/261d1e8bdbca06e85adf3df7a9489bff7ba445ab))
* prod optimizations (GCS ValueError, dynamic profile for fuzzers with big wordlists) ([#707](https://github.com/freelabz/secator/issues/707)) ([bcd6024](https://github.com/freelabz/secator/commit/bcd6024d91362ca141b71a49c4f80c759e1801ca))

## [0.16.4](https://github.com/freelabz/secator/compare/v0.16.3...v0.16.4) (2025-06-13)


### Bug Fixes

* **dalfox:** reduce chunk size for dalfox ([#700](https://github.com/freelabz/secator/issues/700)) ([c14be68](https://github.com/freelabz/secator/commit/c14be68427d18072cf75c61fb6ae966f97515d15))
* **gcs:** add stored_response_path to sent items ([#697](https://github.com/freelabz/secator/issues/697)) ([7c6f992](https://github.com/freelabz/secator/commit/7c6f992b6c7898e956436e169b64af1d9f1d8934))
* mongodb optimizations ([#699](https://github.com/freelabz/secator/issues/699)) ([c0497a6](https://github.com/freelabz/secator/commit/c0497a67c293680dafdc052eff510ffd17edafe6))

## [0.16.3](https://github.com/freelabz/secator/compare/v0.16.2...v0.16.3) (2025-06-11)


### Bug Fixes

* bup file flag ([#690](https://github.com/freelabz/secator/issues/690)) ([83d83d7](https://github.com/freelabz/secator/commit/83d83d72c5c523ea44dcc3cb78f478c935ed4127))
* **celery:** add no_live_updates to skip backend updates ([#695](https://github.com/freelabz/secator/issues/695)) ([c99599c](https://github.com/freelabz/secator/commit/c99599caa219312e8ca2e190d8353960ca4f2633))
* **dalfox:** use jsonl option instead of json ([#692](https://github.com/freelabz/secator/issues/692)) ([c406e34](https://github.com/freelabz/secator/commit/c406e346a4011b0c57efd7b6d5e518ee6d7953e6))
* **mongodb:** add all output types ([#696](https://github.com/freelabz/secator/issues/696)) ([af98935](https://github.com/freelabz/secator/commit/af989352662f53903768c268347e6046db9dd8fd))
* show info message for mark_runner_started / mark_runner_completed ([#694](https://github.com/freelabz/secator/issues/694)) ([ed0f6cb](https://github.com/freelabz/secator/commit/ed0f6cb1464c962fc6f65381762fd23330f9aa85))
* **workflow:** put cariddi in crawlers group ([#693](https://github.com/freelabz/secator/issues/693)) ([a9e1afd](https://github.com/freelabz/secator/commit/a9e1afd97256aefc33d179d9e3d4091f24b332b2))

## [0.16.2](https://github.com/freelabz/secator/compare/v0.16.1...v0.16.2) (2025-06-06)


### Bug Fixes

* run hooks when no_poll is True ([#686](https://github.com/freelabz/secator/issues/686)) ([32e8dba](https://github.com/freelabz/secator/commit/32e8dba71f153a70583855b5401595cedd66b49c))

## [0.16.1](https://github.com/freelabz/secator/compare/v0.16.0...v0.16.1) (2025-06-05)


### Bug Fixes

* maigret output types ([#683](https://github.com/freelabz/secator/issues/683)) ([c3d9193](https://github.com/freelabz/secator/commit/c3d9193662a4272084fa636ad5ac815eddb6afc3))

## [0.16.0](https://github.com/freelabz/secator/compare/v0.15.1...v0.16.0) (2025-06-05)


### Features

* **`dnsx`:** merge `dnsxbrute` into `dnsx` ([#571](https://github.com/freelabz/secator/issues/571)) ([d30a497](https://github.com/freelabz/secator/commit/d30a4974cafba8c5a88afbe41b46f230e0667624))
* add task revoke state and perf improvements ([#678](https://github.com/freelabz/secator/issues/678)) ([2a3bf08](https://github.com/freelabz/secator/commit/2a3bf089a643f889417da447047a6d45818dbb24))
* allow returning errors in hooks ([#632](https://github.com/freelabz/secator/issues/632)) ([39a56bd](https://github.com/freelabz/secator/commit/39a56bdb3d7e3cc91db28f227ee3c8d517319ba2))
* improve bbot output types ([#627](https://github.com/freelabz/secator/issues/627)) ([3b0aa5d](https://github.com/freelabz/secator/commit/3b0aa5de419cdabb4e450373d98942b32f52565d))
* improve runner logic, workflow building, results filtering logic; and add config defaults for profiles & drivers ([#673](https://github.com/freelabz/secator/issues/673)) ([df94657](https://github.com/freelabz/secator/commit/df94657836baf380b0a00bb02467a04bbbb6ea39))
* improve template loading flow ([#667](https://github.com/freelabz/secator/issues/667)) ([f223120](https://github.com/freelabz/secator/commit/f2231200917a2eff1fb35f782739a4ae52b2382b))
* memory optimizations ([#681](https://github.com/freelabz/secator/issues/681)) ([d633133](https://github.com/freelabz/secator/commit/d633133263f0b1bcab54a2a0278b46fa37c5c5ab))
* **misc:** condition-based runs, chunked_by opts, dynamic task profiles, cli improvements ([#659](https://github.com/freelabz/secator/issues/659)) ([e8225cd](https://github.com/freelabz/secator/commit/e8225cd1b434569ecdb6b99f48821bc7c581896e))
* **runner:** add input validation to all tasks and workflows ([#663](https://github.com/freelabz/secator/issues/663)) ([8392551](https://github.com/freelabz/secator/commit/839255108d5a688cad96940bc44f86ff5ae66ba3))
* **runner:** improve option handling ([#670](https://github.com/freelabz/secator/issues/670)) ([59b1c68](https://github.com/freelabz/secator/commit/59b1c68abe90a738dff04ee7a1ef68078ff7fa21))
* **scans:** improve scans ([#660](https://github.com/freelabz/secator/issues/660)) ([bdd38ec](https://github.com/freelabz/secator/commit/bdd38ecbf1f1479dee5f1f39583047f8a6abccd8))
* use os system for CLI and better labs ([#649](https://github.com/freelabz/secator/issues/649)) ([8b49912](https://github.com/freelabz/secator/commit/8b499121e4c646943cb8d692e80e99c85b396d5a))
* **workflow:** improve subdomain_recon workflow ([#657](https://github.com/freelabz/secator/issues/657)) ([bc65092](https://github.com/freelabz/secator/commit/bc6509270031d422ceb0007be415d9cb8066534c))


### Bug Fixes

* allow dry-run mode to work without targets ([#624](https://github.com/freelabz/secator/issues/624)) ([cccffb9](https://github.com/freelabz/secator/commit/cccffb93ba4537887bed656319d47351ba5f8618))
* check task is registered before running test ([1f5cd83](https://github.com/freelabz/secator/commit/1f5cd831c81f8773d619c9f5b4e137f7247ce3e0))
* formatting for dynamic opts ([#628](https://github.com/freelabz/secator/issues/628)) ([dcbbfe9](https://github.com/freelabz/secator/commit/dcbbfe9d7f0acf95c8a5a0ccf787d5c9abcfbcef))
* header options conversion ([#633](https://github.com/freelabz/secator/issues/633)) ([6ae8423](https://github.com/freelabz/secator/commit/6ae8423a75e2cab31ebc90b6b0fdaba44eba430f))
* header parsing ([#629](https://github.com/freelabz/secator/issues/629)) ([db2f028](https://github.com/freelabz/secator/commit/db2f028a40fed0188855299f413b9e12f3dae8cf))
* improve mongodb duplicate checker ([#626](https://github.com/freelabz/secator/issues/626)) ([bf277a9](https://github.com/freelabz/secator/commit/bf277a9d91da263e9ef6fdcd6cb6f15499bfb79d))
* **installer:** compound distro.like() on distribs like popos ([#653](https://github.com/freelabz/secator/issues/653)) ([3687e1d](https://github.com/freelabz/secator/commit/3687e1d54ab5065286952b71c624b2eda276ed50))
* **installer:** ignore dev/post release from PyPI ([#634](https://github.com/freelabz/secator/issues/634)) ([614c3e2](https://github.com/freelabz/secator/commit/614c3e2c20566c7a608816ad504128a10b1923d1))
* **installer:** secator update with correct package version ([#648](https://github.com/freelabz/secator/issues/648)) ([a9cf189](https://github.com/freelabz/secator/commit/a9cf1899cade5d34f25c002eac9feeabbdc6353e))
* lab --wait not in gitlab runner ([070ae84](https://github.com/freelabz/secator/commit/070ae84d4be8b5cfa4e4336a0d089ab12629ba3c))
* logic to test all tasks ([3bd7503](https://github.com/freelabz/secator/commit/3bd7503c100aa4584bd3289a1bab013439e7810a))
* os.system return code ([02aed75](https://github.com/freelabz/secator/commit/02aed757a9a8764c22e28c133c19e5de66b188fb))
* progress type fields ([#652](https://github.com/freelabz/secator/issues/652)) ([f146914](https://github.com/freelabz/secator/commit/f146914f3d947a536ada03201e8f3fdf08615a54))
* remove duplicates from txt exporter ([#630](https://github.com/freelabz/secator/issues/630)) ([88ba5c5](https://github.com/freelabz/secator/commit/88ba5c5c339f91da32b72f17bed54a65988b2d8b))
* remove fping -r flag by default, show alive hosts better ([#665](https://github.com/freelabz/secator/issues/665)) ([5c945fd](https://github.com/freelabz/secator/commit/5c945fdcf1ad7422698fe5519bc5abddcc0473ca))
* remove no-recreate flag in labs as not supported by github runner ([bd997a8](https://github.com/freelabz/secator/commit/bd997a8f8c1607f49418db98ef733caefad6b0b7))
* short opt incorrectly named ([#631](https://github.com/freelabz/secator/issues/631)) ([0c73c60](https://github.com/freelabz/secator/commit/0c73c60380616dfab268d2541f83bf9cf4518098))
* tasks with no file flag need input_chunk_size=1 ([#668](https://github.com/freelabz/secator/issues/668)) ([a088c94](https://github.com/freelabz/secator/commit/a088c949219718757fd1611acf8ddb8167b0deb8))
* tools in readme, arjun chunk and ffuf header  ([#679](https://github.com/freelabz/secator/issues/679)) ([654ff30](https://github.com/freelabz/secator/commit/654ff30ca2ffc1caae7e797df922b86cd83a98ad))
* tools table generator update ([9420f14](https://github.com/freelabz/secator/commit/9420f1426d722079d9058c7b37e4118119dc9542))
* update ci workflow ([f4c2b13](https://github.com/freelabz/secator/commit/f4c2b1300fc7d4417704eee7e9917bf184039feb))
* update generate table workflow ([ff62702](https://github.com/freelabz/secator/commit/ff627029120a146e55e5dbc6b95d1d9adf9cb8fa))
* vulnerability output reference when unset ([#625](https://github.com/freelabz/secator/issues/625)) ([a656fbf](https://github.com/freelabz/secator/commit/a656fbfd306b334fdca72cdc04321cd2e8c749bb))


### Documentation

* generate tools table md ([#610](https://github.com/freelabz/secator/issues/610)) ([d60f11e](https://github.com/freelabz/secator/commit/d60f11ea72999b163e55634c8bdabaf134e3b368))

## [0.15.0](https://github.com/freelabz/secator/compare/v0.14.0...v0.15.0) (2025-05-04)


### Features

* improve cli usage and add multi input types ([#609](https://github.com/freelabz/secator/issues/609)) ([b850914](https://github.com/freelabz/secator/commit/b8509141e62dfd72e0b4f15c2b9b5466089e9818))


### Bug Fixes

* installer issue on non-standard distribs ([#613](https://github.com/freelabz/secator/issues/613)) ([194e911](https://github.com/freelabz/secator/commit/194e911b420fcbb0feec3b563a098a3f36cc09cd))

## [0.14.0](https://github.com/freelabz/secator/compare/v0.13.0...v0.14.0) (2025-04-30)


### Features

* add support for profiles ([#532](https://github.com/freelabz/secator/issues/532)) ([6f499b7](https://github.com/freelabz/secator/commit/6f499b72ec18dddde717e00318be4e2b53cc0478))


### Bug Fixes

* **cli:** restore --unified option, delete port_scan workflow ([#606](https://github.com/freelabz/secator/issues/606)) ([6dc647d](https://github.com/freelabz/secator/commit/6dc647d7205d15faa1c675485af441549d798118))

## [0.13.0](https://github.com/freelabz/secator/compare/v0.12.0...v0.13.0) (2025-04-29)


### Features

* **core:** restore default task opts, improve workflows ([#560](https://github.com/freelabz/secator/issues/560)) ([4849d44](https://github.com/freelabz/secator/commit/4849d44448f52529380a6d9163a1b4db54114958))


### Bug Fixes

* use distro.like() instead of distro.id() ([#604](https://github.com/freelabz/secator/issues/604)) ([15157d4](https://github.com/freelabz/secator/commit/15157d433a0c60292ed91bb26f513a10f15924c2))

## [0.12.0](https://github.com/freelabz/secator/compare/v0.11.1...v0.12.0) (2025-04-24)


### Features

* add --show option to display yaml ([#601](https://github.com/freelabz/secator/issues/601)) ([8edffe9](https://github.com/freelabz/secator/commit/8edffe9f879bb7a99a7e5fead1a18dbf6da5d140))
* **arjun:** add --disable-redirects opts ([#598](https://github.com/freelabz/secator/issues/598)) ([17618c7](https://github.com/freelabz/secator/commit/17618c7ca647536207a96ce2c235ec5227db2cef))
* **workflows:** improve url params fuzz workflow ([#597](https://github.com/freelabz/secator/issues/597)) ([38fa1bc](https://github.com/freelabz/secator/commit/38fa1bcd76c9c6dbe0bc85c9c8c707ae642b9830))


### Bug Fixes

* better options overrides for CLI ([#596](https://github.com/freelabz/secator/issues/596)) ([74e256b](https://github.com/freelabz/secator/commit/74e256b434d36f1e16390f8d06571e726517f5ce))
* worker quiet option ([#602](https://github.com/freelabz/secator/issues/602)) ([9b2c084](https://github.com/freelabz/secator/commit/9b2c08458e3412a89ec39547a728a26885fe1162))

## [0.11.1](https://github.com/freelabz/secator/compare/v0.11.0...v0.11.1) (2025-04-23)


### Bug Fixes

* fping ret code ([#593](https://github.com/freelabz/secator/issues/593)) ([f2d0982](https://github.com/freelabz/secator/commit/f2d0982ea665a08d24afd3f80c8f976811daa397))
* ghsa lookups, startup file downloads ([#592](https://github.com/freelabz/secator/issues/592)) ([021bf11](https://github.com/freelabz/secator/commit/021bf11b6cd7d9ecb5dd95b45d6411d1feeeb86c))
* wordlist dynamic download ([#595](https://github.com/freelabz/secator/issues/595)) ([9a859ae](https://github.com/freelabz/secator/commit/9a859ae8f391bb73263b356ef166f5685683c30f))

## [0.11.0](https://github.com/freelabz/secator/compare/v0.10.0...v0.11.0) (2025-04-22)


### Features

* **celery:** simplify task runner logic ([#574](https://github.com/freelabz/secator/issues/574)) ([9eb057c](https://github.com/freelabz/secator/commit/9eb057cee0afcba93e2f5d7d1d9a4807c1ecb1fc))
* **output_types:** add Certificate output type ([#459](https://github.com/freelabz/secator/issues/459)) ([179f915](https://github.com/freelabz/secator/commit/179f9154d9886245c16b9c38365365b08ee4afb9))
* restore nmap defaults, del port_scan, mod host_recon ([#581](https://github.com/freelabz/secator/issues/581)) ([e0c7c58](https://github.com/freelabz/secator/commit/e0c7c58c11b462ac161263e2550064387b5c0ff5))
* **runner:** core improvements ([#582](https://github.com/freelabz/secator/issues/582)) ([11f2dd3](https://github.com/freelabz/secator/commit/11f2dd3cbcf16139e3495b9cb54da6fdff0d95e6))
* **task:** arjun integration ([#504](https://github.com/freelabz/secator/issues/504)) ([be7f80c](https://github.com/freelabz/secator/commit/be7f80cee0a9251cca6b5e55f4293e8881516f7a))
* **tasks:** add wpprobe ([#557](https://github.com/freelabz/secator/issues/557)) ([d413097](https://github.com/freelabz/secator/commit/d4130971ac0b7fc9f6e357d3e0f17fc6d6d60004))
* **tasks:** gitleaks integration ([#441](https://github.com/freelabz/secator/issues/441)) ([e6d5830](https://github.com/freelabz/secator/commit/e6d58308a64dc018c1706854795eac2c6d88adc4))
* **tasks:** trivy integration ([#460](https://github.com/freelabz/secator/issues/460)) ([f7169cf](https://github.com/freelabz/secator/commit/f7169cfdb32697b25c59f1106b8da80eb6540ab2))
* **tasks:** wafw00f integration ([#471](https://github.com/freelabz/secator/issues/471)) ([b9b80b0](https://github.com/freelabz/secator/commit/b9b80b06449f863b117350e4be3acb9f14a59ca8))
* **task:** testssl.sh integration ([#484](https://github.com/freelabz/secator/issues/484)) ([7c65d60](https://github.com/freelabz/secator/commit/7c65d605eedc0f63ace2724fff5b584314065ccb))


### Bug Fixes

* add debug of tasks unit tests, internal tasks not added to cmd, add display flag for options ([#587](https://github.com/freelabz/secator/issues/587)) ([3980234](https://github.com/freelabz/secator/commit/3980234d968a893940736daa2bb347951190bce1))
* add default user agent and remove ffuf recursion ([#586](https://github.com/freelabz/secator/issues/586)) ([332d1bd](https://github.com/freelabz/secator/commit/332d1bd4a63f8338bc9425ccd92d5188fc6e983e))
* **celery:** kill worker in solo mode ([#568](https://github.com/freelabz/secator/issues/568)) ([c2fd107](https://github.com/freelabz/secator/commit/c2fd107ea1c4248c3eba518dfdc6d777eff8ef15))
* help shorthand flag -h ([#591](https://github.com/freelabz/secator/issues/591)) ([ea3a4ce](https://github.com/freelabz/secator/commit/ea3a4ceb4c8dec14caf2fdde7e6ad39b03695cfd))
* installer and x-platform issues ([#590](https://github.com/freelabz/secator/issues/590)) ([8ce1e1e](https://github.com/freelabz/secator/commit/8ce1e1eaf2e80249060035ffe27fef330c54f366))
* **installer:** support single binary download ([#588](https://github.com/freelabz/secator/issues/588)) ([bc799b9](https://github.com/freelabz/secator/commit/bc799b9da4e34b8974d92790ac185db4f5884472))
* thread is_started ([9b6c6bb](https://github.com/freelabz/secator/commit/9b6c6bb244a3434db3d398160918bc807288a9ad))
* wordlist not loaded when local path is provided ([#572](https://github.com/freelabz/secator/issues/572)) ([ef071a9](https://github.com/freelabz/secator/commit/ef071a9aa430220b5cfe0dcb5db271512339a140))
* wpscan ignore main redirect and ssl ignore ([#577](https://github.com/freelabz/secator/issues/577)) ([35c445d](https://github.com/freelabz/secator/commit/35c445dc9a669c8f73764b712c13e983d7598f90))

## [0.10.0](https://github.com/freelabz/secator/compare/v0.9.4...v0.10.0) (2025-03-04)


### Features

* **celery:** add single pool job processing options ([#558](https://github.com/freelabz/secator/issues/558)) ([cca9797](https://github.com/freelabz/secator/commit/cca9797339ed95c15ef42604ba9bf897a76da766))


### Bug Fixes

* add poll queue and re-route tasks to it when chunked ([#562](https://github.com/freelabz/secator/issues/562)) ([b9e7576](https://github.com/freelabz/secator/commit/b9e7576dcd46db0e95df09dc8beafb762314cc39))
* **config:** disable key not found error message (too verbose) ([#563](https://github.com/freelabz/secator/issues/563)) ([3b044da](https://github.com/freelabz/secator/commit/3b044da14f3e399e03e10c97566a25e858e7e7d6))
* **katana:** add -no-sandbox option ([#566](https://github.com/freelabz/secator/issues/566)) ([50cf2fe](https://github.com/freelabz/secator/commit/50cf2fef5eaa1b7cf67c691360e3349b7bf7bfbe))
* mongodb document bug ([#564](https://github.com/freelabz/secator/issues/564)) ([29c6af4](https://github.com/freelabz/secator/commit/29c6af4f3a2a49ac973f7193ca334f56e7b178d5))
* reset nuclei input chunk size ([#561](https://github.com/freelabz/secator/issues/561)) ([683b9ef](https://github.com/freelabz/secator/commit/683b9efb28d2425961e2e64c31b9af5cb07c0923))

## [0.9.4](https://github.com/freelabz/secator/compare/v0.9.3...v0.9.4) (2025-02-25)


### Bug Fixes

* **nuclei:** set input_chunk_size to 1 ([cf6bda1](https://github.com/freelabz/secator/commit/cf6bda19e97754a3560e2ed17bfb83c87d889f1e))

## [0.9.4](https://github.com/freelabz/secator/compare/v0.9.3...v0.9.4) (2025-02-25)


### Bug Fixes

* **nuclei:** set input_chunk_size to 1 ([cf6bda1](https://github.com/freelabz/secator/commit/cf6bda19e97754a3560e2ed17bfb83c87d889f1e))

## [0.9.3](https://github.com/freelabz/secator/compare/v0.9.2...v0.9.3) (2025-02-24)


### Bug Fixes

* add celery monitoring opts ([#552](https://github.com/freelabz/secator/issues/552)) ([51681d3](https://github.com/freelabz/secator/commit/51681d3dad12570a6483c30dda82a40e81675c2e))
* update tasks profiles ([#553](https://github.com/freelabz/secator/issues/553)) ([cebc50a](https://github.com/freelabz/secator/commit/cebc50a9139f31f5315e5e290e90807744df9db3))

## [0.9.2](https://github.com/freelabz/secator/compare/v0.9.1...v0.9.2) (2025-02-23)


### Bug Fixes

* warning bug ([#550](https://github.com/freelabz/secator/issues/550)) ([3853d47](https://github.com/freelabz/secator/commit/3853d4781f4b135ddbf5eab8ccaf5bbf02feb2e0))

## [0.9.1](https://github.com/freelabz/secator/compare/v0.9.0...v0.9.1) (2025-02-22)


### Bug Fixes

* add celery broker transport options ([#547](https://github.com/freelabz/secator/issues/547)) ([3703d1e](https://github.com/freelabz/secator/commit/3703d1e10dd605b9c631ff6084713beb36bda469))
* add celery opts required for remote ([#544](https://github.com/freelabz/secator/issues/544)) ([36d1f2d](https://github.com/freelabz/secator/commit/36d1f2dadbd601ad8866e0b4ada485e3d26ec1b6))
* bbot port not cast as int ([#542](https://github.com/freelabz/secator/issues/542)) ([744553c](https://github.com/freelabz/secator/commit/744553c597869e0c4811214a00ead740b4dcd2e9))
* change main dockerfile path ([#546](https://github.com/freelabz/secator/issues/546)) ([6a2faf6](https://github.com/freelabz/secator/commit/6a2faf6966db2bf340311815a46ff4c347c8c136))
* cli bug warning ([#543](https://github.com/freelabz/secator/issues/543)) ([ca44b12](https://github.com/freelabz/secator/commit/ca44b12dcc5e4869753dc1d186adabd77825ee7e))
* update Dockerfile symlink ([#549](https://github.com/freelabz/secator/issues/549)) ([1b2bdcf](https://github.com/freelabz/secator/commit/1b2bdcf37eabad7150420a8893bb064a9f9c41cb))
* **wpscan:** set vuln confidence ([#548](https://github.com/freelabz/secator/issues/548)) ([0d8f13d](https://github.com/freelabz/secator/commit/0d8f13d7830906654778910c3e0e259962e31276))

## [0.9.0](https://github.com/freelabz/secator/compare/v0.8.2...v0.9.0) (2025-02-21)


### Features

* add cleanup option to secator install tools ([#530](https://github.com/freelabz/secator/issues/530)) ([bcc11c2](https://github.com/freelabz/secator/commit/bcc11c24e628b527111b1890b3810bf60be14448))
* add warning if bin dir is not in path ([#528](https://github.com/freelabz/secator/issues/528)) ([59ca31e](https://github.com/freelabz/secator/commit/59ca31e3e4bb07680762213d6f5722afb9586519))
* improve dockerfile size with multi-stage build ([#534](https://github.com/freelabz/secator/issues/534)) ([ceb3652](https://github.com/freelabz/secator/commit/ceb3652371669bfce525a5e26c38e88e9e03356f))


### Bug Fixes

* bbot screenshots copy ([#540](https://github.com/freelabz/secator/issues/540)) ([2cea982](https://github.com/freelabz/secator/commit/2cea9825cf73fb97546c38793c7f280db7c99822))
* install chromium in httpx ([#541](https://github.com/freelabz/secator/issues/541)) ([1965619](https://github.com/freelabz/secator/commit/19656198351fc0b40f71aeb7fb20035db6b89a37))
* miscellaneous bugfixes ([#533](https://github.com/freelabz/secator/issues/533)) ([b8c0edf](https://github.com/freelabz/secator/commit/b8c0edf30882bb030dbb6b376e264850d3905307))
* restore colors to rich defaults to honor TERM and NO_COLOR ([#524](https://github.com/freelabz/secator/issues/524)) ([982fc55](https://github.com/freelabz/secator/commit/982fc55a60c03d03bf871727fafdf6840dab0908))
* secator update command ([#538](https://github.com/freelabz/secator/issues/538)) ([cf73def](https://github.com/freelabz/secator/commit/cf73def36de7e9e8522d795922daae02252792fd))

## [0.8.2](https://github.com/freelabz/secator/compare/v0.8.1...v0.8.2) (2025-02-10)


### Bug Fixes

* random proxy bug ([#433](https://github.com/freelabz/secator/issues/433)) ([a437684](https://github.com/freelabz/secator/commit/a4376844b7dea55e8951fe578d5631688728e503))

## [0.8.1](https://github.com/freelabz/secator/compare/v0.8.0...v0.8.1) (2025-02-07)


### Bug Fixes

* reduce docker image size ([#516](https://github.com/freelabz/secator/issues/516)) ([28d8fa3](https://github.com/freelabz/secator/commit/28d8fa379a88a1af73df7edfda28c0270f521bb4))

## [0.8.0](https://github.com/freelabz/secator/compare/v0.7.0...v0.8.0) (2025-02-06)


### Features

* add alpine to msfinstall script ([cf921fd](https://github.com/freelabz/secator/commit/cf921fd7e7f31f6e37c14e5831f5e4d3aa087f44))
* add install support for multiple distribs ([#514](https://github.com/freelabz/secator/issues/514)) ([19d1317](https://github.com/freelabz/secator/commit/19d131760221cf6c92a6f60e29ceb236eb7e0640))
* **config:** load wordlists from URLs and config values ([#498](https://github.com/freelabz/secator/issues/498)) ([d537952](https://github.com/freelabz/secator/commit/d537952cc0065de2053479ab75927321b8032e41))
* **nmap:** lookup and correlate exploits with CVE ids ([#489](https://github.com/freelabz/secator/issues/489)) ([988edcb](https://github.com/freelabz/secator/commit/988edcbb1f5855f64a96dd5b1cc16c0c10256cc6))
* **runner:** add previous results to runner results ([#503](https://github.com/freelabz/secator/issues/503)) ([2c490fb](https://github.com/freelabz/secator/commit/2c490fb2d5d358785c22849716f78f158c975766))


### Bug Fixes

* **cli:** various fixes to report commands ([#507](https://github.com/freelabz/secator/issues/507)) ([ee715dd](https://github.com/freelabz/secator/commit/ee715dd9cba75a1e1a3ff12ec98ccbdae8c48675))
* **docs:** update docker-compose.yml ([#462](https://github.com/freelabz/secator/issues/462)) ([3140ee2](https://github.com/freelabz/secator/commit/3140ee25dd69aa387e3b100719a67609c099219b))
* **install:** strict healthcheck, better version parsing, install fixes ([#496](https://github.com/freelabz/secator/issues/496)) ([7d6e071](https://github.com/freelabz/secator/commit/7d6e0719dc3a83fb6ae47b2898bb63d43c03f685))
* misc bug fixes ([#511](https://github.com/freelabz/secator/issues/511)) ([16b50c4](https://github.com/freelabz/secator/commit/16b50c481da5be9b62cbb93effd9464a581e57a6))
* **msfconsole:** bug fixes ([#488](https://github.com/freelabz/secator/issues/488)) ([a54077d](https://github.com/freelabz/secator/commit/a54077d5cbcf5518f73300edf4db9a2000017ec5))
* msfinstall script ([171f868](https://github.com/freelabz/secator/commit/171f868d07c4c29444fca7487b7ea9d25148b295))
* **naabu:** change localhost to 127.0.0.1 before run ([#501](https://github.com/freelabz/secator/issues/501)) ([d0938ba](https://github.com/freelabz/secator/commit/d0938bac31de3d820e6dee53b61f9458fcd1a424))
* **naabu:** convert localhost to 127.0.0.1 and back ([#502](https://github.com/freelabz/secator/issues/502)) ([935ee65](https://github.com/freelabz/secator/commit/935ee65c13db90e8e6479d189947b48302fb5db1))
* **runner:** duplicate prints in runner due to processing of existing results ([#509](https://github.com/freelabz/secator/issues/509)) ([602cdf0](https://github.com/freelabz/secator/commit/602cdf0445a5ece0c1d50ae04ff1266705cff71b))
* syntax warnings ([#508](https://github.com/freelabz/secator/issues/508)) ([54fb8cd](https://github.com/freelabz/secator/commit/54fb8cdb3f8f8cd3a42a28ce5f8d5f45e9c50295))
* **template:** bugfix for compound group keys ([#487](https://github.com/freelabz/secator/issues/487)) ([b3e7327](https://github.com/freelabz/secator/commit/b3e73274426f09a5e940f5932ae09e7eb1f592d7))
* **tests:** update wpscan integration test ([#490](https://github.com/freelabz/secator/issues/490)) ([1493063](https://github.com/freelabz/secator/commit/1493063f236f33f6ed1ec37a1359e859f51ecd53))
* update cve circl search ([#506](https://github.com/freelabz/secator/issues/506)) ([6e10e4a](https://github.com/freelabz/secator/commit/6e10e4aa2f7013dce4941688d98bda0253588bfc))
* various fixes ([#515](https://github.com/freelabz/secator/issues/515)) ([a88c5a7](https://github.com/freelabz/secator/commit/a88c5a7e9a0ec01f4824e427474a7bd115008b5d))

## [0.7.0](https://github.com/freelabz/secator/compare/v0.6.0...v0.7.0) (2024-11-13)


### Features

* **`bup`:** add proxy option and progress indicator ([#444](https://github.com/freelabz/secator/issues/444)) ([d5c63c8](https://github.com/freelabz/secator/commit/d5c63c81c6465a142ce70e4800effc02d526a243))
* **`dnsx`:** add IP output type on dnsx A record  ([#426](https://github.com/freelabz/secator/issues/426)) ([629439e](https://github.com/freelabz/secator/commit/629439e459a6eefd5cbe68e9fc3a317371ba7987))
* **`naabu`/`nmap`:** help for defaults and change workflow opts ([#438](https://github.com/freelabz/secator/issues/438)) ([4dd0055](https://github.com/freelabz/secator/commit/4dd00556648e691a093887d294325b00409ac04a))
* **`nmap`:** add udp scan (`-sU`) and change default scan opts ([#418](https://github.com/freelabz/secator/issues/418)) ([36c6ff3](https://github.com/freelabz/secator/commit/36c6ff3766f88ac311c1bfea86a1b5e8686dd94e))
* add url_bypass workflow based on bup ([e96b1bc](https://github.com/freelabz/secator/commit/e96b1bc9906cd2f9aa3eb5b3770594811f242abd))
* chunk dalfox input by 1 ([#443](https://github.com/freelabz/secator/issues/443)) ([26c38d7](https://github.com/freelabz/secator/commit/26c38d79e89be3d35f464e89c6973b7beadb6ac4))
* **cli:** misc bug fixes and features ([#445](https://github.com/freelabz/secator/issues/445)) ([fccfdb8](https://github.com/freelabz/secator/commit/fccfdb8ca38dcd3a2c559429a7d58d46ecac49a6))
* **hooks:** explicit output type yield in static hooks ([#439](https://github.com/freelabz/secator/issues/439)) ([2d1f8e6](https://github.com/freelabz/secator/commit/2d1f8e6b7b77210028efe2c2c56866efbd6b0152))
* **katana:** add form_fill option ([#419](https://github.com/freelabz/secator/issues/419)) ([bebddb1](https://github.com/freelabz/secator/commit/bebddb1e2fae460403adda2d84b9ae515ca977aa))
* **refactor:** improve performance, add on_interval hook, rework CLI opts ([#473](https://github.com/freelabz/secator/issues/473)) ([4a22a70](https://github.com/freelabz/secator/commit/4a22a7082fe1edf50644034cfc54b11653b47aa4))
* **runner:** add GCS driver and secator threads ([#476](https://github.com/freelabz/secator/issues/476)) ([cae475a](https://github.com/freelabz/secator/commit/cae475a2fe15742ccd80d40c28ad41aa1ffc5348))
* **runner:** add skip_if_no_inputs to workflows ([#482](https://github.com/freelabz/secator/issues/482)) ([5546b82](https://github.com/freelabz/secator/commit/5546b82756d6aad0d227072d5a3b1149c44306e8))
* **runner:** on serialized hooks ([#424](https://github.com/freelabz/secator/issues/424)) ([fde6cd7](https://github.com/freelabz/secator/commit/fde6cd7f6cba015b08b370bfd14b0aca3f4a4018))
* **runner:** rework Celery core and mix fixes ([#450](https://github.com/freelabz/secator/issues/450)) ([b72f152](https://github.com/freelabz/secator/commit/b72f15286bb29ae60568309907d4dad41d4fbacb))
* sudo prompt check test ([#432](https://github.com/freelabz/secator/issues/432)) ([f45b123](https://github.com/freelabz/secator/commit/f45b1230fd6313342ebdda5a359c1285f2d80aa8))
* sudo prompts in non-tty mode ([#431](https://github.com/freelabz/secator/issues/431)) ([0e26b55](https://github.com/freelabz/secator/commit/0e26b55c168bfd69c212bc7667ef1b97e89e6bd5))
* **tasks:** bbot integration ([#375](https://github.com/freelabz/secator/issues/375)) ([2f0dea4](https://github.com/freelabz/secator/commit/2f0dea4f4cac3370129d0adf0000c8d0efa54361))
* **tasks:** bup integration ([#398](https://github.com/freelabz/secator/issues/398)) ([ed636aa](https://github.com/freelabz/secator/commit/ed636aad7d90baa7b3b73baebc8f5be002dd796a))


### Bug Fixes

* **cli:** proper opts override for workflows ([#436](https://github.com/freelabz/secator/issues/436)) ([1d1eaa3](https://github.com/freelabz/secator/commit/1d1eaa3283b3d5e9650b452e3865476e6a60a086))
* **dalfox:** restore input_chunk_size to default ([8f0a3b4](https://github.com/freelabz/secator/commit/8f0a3b4976e20afc2fb708483c7f8885b2b9f3d9))
* dnsx parsing output loading error ([#422](https://github.com/freelabz/secator/issues/422)) ([b9e98da](https://github.com/freelabz/secator/commit/b9e98da2b5378957076e1d8f0afd3948d5bcb5f6))
* empty CVE should pass ([#478](https://github.com/freelabz/secator/issues/478)) ([0644d68](https://github.com/freelabz/secator/commit/0644d68ccb92a4c38e8210e39f14f0850d84348d))
* gcs bug with empty paths ([549ac4c](https://github.com/freelabz/secator/commit/549ac4c8e7391a829cf1a6c5a43ad291bec1b34a))
* gcs bug with empty paths ([2d57e1a](https://github.com/freelabz/secator/commit/2d57e1ad4669587cf0abb0a59b0918cf72107d72))
* get_opt_value default value and reorg hooks ([#429](https://github.com/freelabz/secator/issues/429)) ([a44a36d](https://github.com/freelabz/secator/commit/a44a36d37f888787927ec6dfc891e86dab071aa4))
* mix bugfixes for stable release ([b743925](https://github.com/freelabz/secator/commit/b7439258c9cdadc7bd14a0a0b49e2db2d0f5b537))
* nmap defaults ([396f68a](https://github.com/freelabz/secator/commit/396f68a325a5a8f1a9379d314979dbf85a9c95c7))
* **nmap:** undefined service name ([#437](https://github.com/freelabz/secator/issues/437)) ([596f1af](https://github.com/freelabz/secator/commit/596f1aff53e9add73e1587497aee82465d212300))
* runner opts processing ([#477](https://github.com/freelabz/secator/issues/477)) ([d788e9d](https://github.com/freelabz/secator/commit/d788e9d3e508a849119d418bcc5ce371c6c53c6c))
* runner toDict() errors ([#475](https://github.com/freelabz/secator/issues/475)) ([b43c866](https://github.com/freelabz/secator/commit/b43c8669808651368536fa121be2ce79de7556aa))
* **runner:** bug with no inputs ([#483](https://github.com/freelabz/secator/issues/483)) ([4db7b46](https://github.com/freelabz/secator/commit/4db7b460a949e6b74b5837f0f1e3b5ca51b39094))
* **url_vuln:** repair bad condition ([214c8ab](https://github.com/freelabz/secator/commit/214c8abf7cad4916c8301ff056d894cc0bc26b28))


### Documentation

* add package json ([#415](https://github.com/freelabz/secator/issues/415)) ([f9a7c2f](https://github.com/freelabz/secator/commit/f9a7c2fc5df11506cce0d81babf1f7790b80465a))

## [0.6.0](https://github.com/freelabz/secator/compare/v0.5.2...v0.6.0) (2024-07-25)


### Features

* add duplicate finder to mongodb hooks ([#409](https://github.com/freelabz/secator/issues/409)) ([fb0e11c](https://github.com/freelabz/secator/commit/fb0e11cd2b64bf51bc862f47243c8c0602d3d5e9))
* basic helm chart ([#408](https://github.com/freelabz/secator/issues/408)) ([6b2f84f](https://github.com/freelabz/secator/commit/6b2f84f61bd8eccf2cdd61b6ffdc2eb4489240bc))


### Bug Fixes

* Dockerfile broken apt install ([#407](https://github.com/freelabz/secator/issues/407)) ([c023279](https://github.com/freelabz/secator/commit/c02327968ecea816004636801684b336735df439))
* **tasks:** duplicate meta opt entry ([#401](https://github.com/freelabz/secator/issues/401)) ([ae56aa6](https://github.com/freelabz/secator/commit/ae56aa62f5a18936a1787547e37bbe636e6e43c3))

## [0.5.2](https://github.com/freelabz/secator/compare/v0.5.1...v0.5.2) (2024-05-07)


### Bug Fixes

* **nuclei,katana:** add -sr flag and write http responses and screenshot to correct folder ([#395](https://github.com/freelabz/secator/issues/395)) ([1a51790](https://github.com/freelabz/secator/commit/1a51790c9231f593631c2780b6d5e0fa89f1aa55))

## [0.5.1](https://github.com/freelabz/secator/compare/v0.5.0...v0.5.1) (2024-05-06)


### Bug Fixes

* **output:** add headers to Url and print HTTP method when not GET ([#390](https://github.com/freelabz/secator/issues/390)) ([5a87d7b](https://github.com/freelabz/secator/commit/5a87d7b8bc1dd098999f3864952e98068fd32efc))
* **report:** do not remove duplicate in reports by default ([#392](https://github.com/freelabz/secator/issues/392)) ([7d74ae8](https://github.com/freelabz/secator/commit/7d74ae80bfd99c31714a5e7e25f2bd1caa642eb4))

## [0.5.0](https://github.com/freelabz/secator/compare/v0.4.1...v0.5.0) (2024-05-03)


### Features

* add searchsploit output fields ([#278](https://github.com/freelabz/secator/issues/278)) ([00872c4](https://github.com/freelabz/secator/commit/00872c4a7f9b1ec76ee1bfd7a00919d53cbdb30a))
* **cli:** add report list / export commands ([#367](https://github.com/freelabz/secator/issues/367)) ([ab396a3](https://github.com/freelabz/secator/commit/ab396a3098c6d4c46cf9c9b29bd5c54579421646))
* **config:** load external tasks from template dir ([#373](https://github.com/freelabz/secator/issues/373)) ([0c63c02](https://github.com/freelabz/secator/commit/0c63c02c8eca477a6752f4af466c4303801019de))


### Bug Fixes

* **cli:** catch JSON parse errors ([#378](https://github.com/freelabz/secator/issues/378)) ([5e3d7f2](https://github.com/freelabz/secator/commit/5e3d7f2d2938a857e7599a429a6cfabf3b12347b))
* **nmap:** resolve -sS tcp syn stealth issue ([#376](https://github.com/freelabz/secator/issues/376)) ([a3efc65](https://github.com/freelabz/secator/commit/a3efc651dfa4d8fa34d611b9aea2e156352fdc45))

## [0.4.1](https://github.com/freelabz/secator/compare/v0.4.0...v0.4.1) (2024-04-30)


### Bug Fixes

* failed addons import ([#368](https://github.com/freelabz/secator/issues/368)) ([aee7ede](https://github.com/freelabz/secator/commit/aee7edeee1e96292e637b9161034f0d628a1f386))
* load dotenv before config import ([#370](https://github.com/freelabz/secator/issues/370)) ([ba2ea8e](https://github.com/freelabz/secator/commit/ba2ea8e3624dda7268d3788c0541fc0d37195358))

## [0.4.0](https://github.com/freelabz/secator/compare/v0.3.6...v0.4.0) (2024-04-27)


### Features

* `nuclei` - add "meta" items to extra_data ([#329](https://github.com/freelabz/secator/issues/329)) ([d986e01](https://github.com/freelabz/secator/commit/d986e01ed10bfd58c57565e24f053cf4ffb165b5))
* add offline mode ([#314](https://github.com/freelabz/secator/issues/314)) ([6b55e99](https://github.com/freelabz/secator/commit/6b55e99a9e60a102afaf71a49148a8aec1b2e3dc))
* add secator configuration loader ([#313](https://github.com/freelabz/secator/issues/313)) ([9b9ab7b](https://github.com/freelabz/secator/commit/9b9ab7b1c394bd77c986fcb755d19d1b887228cf))


### Bug Fixes

* add alias for config command and reload help screenshot ([#324](https://github.com/freelabz/secator/issues/324)) ([3dbc9ad](https://github.com/freelabz/secator/commit/3dbc9adf7a3b12dbf5bdcaa2224297d58b1e2fd8))
* add nmap --top-ports option ([#339](https://github.com/freelabz/secator/issues/339)) ([6352be7](https://github.com/freelabz/secator/commit/6352be7350890c38e521d98b89e7e634ed8c8684))
* add redis addon missing warning on celery worker ([#310](https://github.com/freelabz/secator/issues/310)) ([c0afc3a](https://github.com/freelabz/secator/commit/c0afc3a068140f9811845c05c8d3763d932407de))
* better vuln detection ([#349](https://github.com/freelabz/secator/issues/349)) ([150b603](https://github.com/freelabz/secator/commit/150b6030e6702f599b8a67ba53bef4c2e675e90a))
* **config:** broken list values with 0 or 1 element ([#364](https://github.com/freelabz/secator/issues/364)) ([7ef7a5e](https://github.com/freelabz/secator/commit/7ef7a5e27604df53868d2b670439a0a7150e8af1))
* **docker:** pull remote DockerHub images in Compose ([#363](https://github.com/freelabz/secator/issues/363)) ([dce6d8a](https://github.com/freelabz/secator/commit/dce6d8a5d722aa85c1fc2592f44738b6bfe79b04))
* grype integration test ([#327](https://github.com/freelabz/secator/issues/327)) ([33ddb84](https://github.com/freelabz/secator/commit/33ddb84836965c4bff6fd442c317de240e54ec3f))
* minor config tweaks ([#360](https://github.com/freelabz/secator/issues/360)) ([4631024](https://github.com/freelabz/secator/commit/46310245afe0b0d04a6b333175f28ffeab1659bb))
* next steps highlight ([#326](https://github.com/freelabz/secator/issues/326)) ([528c715](https://github.com/freelabz/secator/commit/528c715e4f20bceb9dbae85e99b707243d556aea))
* proper local file naming for sudo_killer.zip ([#330](https://github.com/freelabz/secator/issues/330)) ([f7e563f](https://github.com/freelabz/secator/commit/f7e563f3a4a20fd38f7167e2bd682ddb3eea6224))
* query CVEs without CPE match ([#321](https://github.com/freelabz/secator/issues/321)) ([d02e09c](https://github.com/freelabz/secator/commit/d02e09cc379afa85df25227f6c0bab4496031d78))
* switch payload sudo_killer to zip ([#318](https://github.com/freelabz/secator/issues/318)) ([2a92dc8](https://github.com/freelabz/secator/commit/2a92dc8d4a71cce71a85bb77747b8af2d5aed6c4))
* task description in remote mode ([#344](https://github.com/freelabz/secator/issues/344)) ([1140611](https://github.com/freelabz/secator/commit/1140611a1129c19bd306db33396ea3fa1bc88f25))
* truncated pickle error ([#334](https://github.com/freelabz/secator/issues/334)) ([663af17](https://github.com/freelabz/secator/commit/663af1777d07c7628a220ee627aece9fc83e6095))


### Documentation

* add VHS demo ([#293](https://github.com/freelabz/secator/issues/293)) ([70454a6](https://github.com/freelabz/secator/commit/70454a60053ef6ce3002565c07ede7b00b14e335))
* update README.md ([a0a19fb](https://github.com/freelabz/secator/commit/a0a19fb24cd297e98cb8716e691ed6fcf11475c6))
* update README.md ([341f5b8](https://github.com/freelabz/secator/commit/341f5b8cd049fd8e33ebfb525de0377d0a659df2))
* Update README.md ([98c986c](https://github.com/freelabz/secator/commit/98c986c644bbe62434c0a2fe72fe9eea606c2e8d))

## [0.3.6](https://github.com/freelabz/secator/compare/v0.3.5...v0.3.6) (2024-04-17)


### Bug Fixes

* broken reports folder on remote workers ([#307](https://github.com/freelabz/secator/issues/307)) ([9a7a1f1](https://github.com/freelabz/secator/commit/9a7a1f1c449c688701b02be66e98d3434073bbb0))
* searchsploit install ([#306](https://github.com/freelabz/secator/issues/306)) ([040cfaf](https://github.com/freelabz/secator/commit/040cfaf6968ae120241fdd6a74a9a6cd5fa0631d))

## [0.3.5](https://github.com/freelabz/secator/compare/v0.3.4...v0.3.5) (2024-04-17)


### Bug Fixes

* Celery control folder ([#298](https://github.com/freelabz/secator/issues/298)) ([3cbc0a3](https://github.com/freelabz/secator/commit/3cbc0a37d06c9b3a20eb0005b1cb68b484d22d15))
* remove pkg_resources in favor of packaging ([#304](https://github.com/freelabz/secator/issues/304)) ([6cf478c](https://github.com/freelabz/secator/commit/6cf478c1f1c4b7363d1710e634686ede8a209594))
* typo in `requires-python` in pyproject.toml ([#303](https://github.com/freelabz/secator/issues/303)) ([7a7766c](https://github.com/freelabz/secator/commit/7a7766caba0faa98406764fa1bb5ad2eae346302))


### Documentation

* update README.md ([8f1b1c1](https://github.com/freelabz/secator/commit/8f1b1c1cb852a88d80aa15379962aaa36afc7635))
* update SECURITY.md ([6518dd6](https://github.com/freelabz/secator/commit/6518dd646c0358e661e186edf28b4fb0494bf712))

## [0.3.4](https://github.com/freelabz/secator/compare/v0.3.3...v0.3.4) (2024-04-15)


### Bug Fixes

* install cariddi from GitHub releases ([#290](https://github.com/freelabz/secator/issues/290)) ([21c9078](https://github.com/freelabz/secator/commit/21c90787713fc08fcf375b37b144a4b86ebc49ee))
* install cariddi from GitHub releases ([#292](https://github.com/freelabz/secator/issues/292)) ([8be216b](https://github.com/freelabz/secator/commit/8be216b01cb2fbc82aca7be32fc190adf17bda52))

## [0.3.3](https://github.com/freelabz/secator/compare/v0.3.2...v0.3.3) (2024-04-13)


### Bug Fixes

* tools install ([#288](https://github.com/freelabz/secator/issues/288)) ([0608a1f](https://github.com/freelabz/secator/commit/0608a1f408551942fca3c729b975b1acbb588903))


### Documentation

* update Docker instructions ([21afd3f](https://github.com/freelabz/secator/commit/21afd3fea06bb2f8ca11a37ec14a5a78d5c0ecb1))

## [0.3.2](https://github.com/freelabz/secator/compare/v0.3.1...v0.3.2) (2024-04-12)


### Bug Fixes

* do not create scripts/ folder ([#273](https://github.com/freelabz/secator/issues/273)) ([8fdaf09](https://github.com/freelabz/secator/commit/8fdaf09d4d1f3fbac7def995b99e9bc4f4f5020d))
* health table padding ([#274](https://github.com/freelabz/secator/issues/274)) ([4f976bd](https://github.com/freelabz/secator/commit/4f976bdaecef7c29a2c6b21ddb29299745dfe5c9))
* install script ([#276](https://github.com/freelabz/secator/issues/276)) ([e27b339](https://github.com/freelabz/secator/commit/e27b3391ea3a5c5a7898d3c02a5f409be44255f8))


### Documentation

* update docker setup ([#279](https://github.com/freelabz/secator/issues/279)) ([9b56e75](https://github.com/freelabz/secator/commit/9b56e75b114f294d222660dbae4f2e6b5e1369cd))

## [0.3.1](https://github.com/freelabz/secator/compare/v0.3.0...v0.3.1) (2024-04-11)


### Bug Fixes

* download default wordlists if missing ([#261](https://github.com/freelabz/secator/issues/261)) ([7bec2a4](https://github.com/freelabz/secator/commit/7bec2a46d054aa7d3702eb77d25b9f791f5cc9c5))
* rework init & tools install ([#271](https://github.com/freelabz/secator/issues/271)) ([6c477fc](https://github.com/freelabz/secator/commit/6c477fc99d5f1dd625423ba27dc563acc50194bf))
* wrong hook name in debug output ([#262](https://github.com/freelabz/secator/issues/262)) ([f2ee367](https://github.com/freelabz/secator/commit/f2ee36779615bd2c1ef1f80679a9cc77e9e592d6))

## [0.3.0](https://github.com/freelabz/secator/compare/v0.2.0...v0.3.0) (2024-04-09)


### Features

* add health command and update check ([#258](https://github.com/freelabz/secator/issues/258)) ([289b86a](https://github.com/freelabz/secator/commit/289b86ac2c278f02102d8824d3de5cf71e3778ae))
* rework install to use pre-packaged binaries when possible ([#253](https://github.com/freelabz/secator/issues/253)) ([b391fe8](https://github.com/freelabz/secator/commit/b391fe8cfdf991b50435c4f53f470e3cea0150ee))


### Bug Fixes

* health -json output ([#257](https://github.com/freelabz/secator/issues/257)) ([4477bb2](https://github.com/freelabz/secator/commit/4477bb25170e80fca1be5985a3b198dd7b423e5f))
* txt output bug ([#256](https://github.com/freelabz/secator/issues/256)) ([fca301d](https://github.com/freelabz/secator/commit/fca301d24c5d9999fef9ae13b8e64c099a65ab95))

## [0.2.0](https://github.com/freelabz/secator/compare/v0.1.1...v0.2.0) (2024-04-08)


### Features

* add build & release CLI commands ([#247](https://github.com/freelabz/secator/issues/247)) ([775eba1](https://github.com/freelabz/secator/commit/775eba16d3a6f9d8cbc83f81daed85fb806fe6db))


### Bug Fixes

* docker build & push ([#250](https://github.com/freelabz/secator/issues/250)) ([7cebd9f](https://github.com/freelabz/secator/commit/7cebd9fe61f6dbb76e9f78fcbcd3514d68204c87))
* install issues & docs ([#243](https://github.com/freelabz/secator/issues/243)) ([0447148](https://github.com/freelabz/secator/commit/0447148c89f13884cbc14579d953e0d3e067cbe2)), closes [#242](https://github.com/freelabz/secator/issues/242) [#241](https://github.com/freelabz/secator/issues/241) [#240](https://github.com/freelabz/secator/issues/240) [#239](https://github.com/freelabz/secator/issues/239)
