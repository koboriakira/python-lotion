# Changelog

## [0.8.2](https://github.com/koboriakira/python-lotion/compare/v0.8.1...v0.8.2) (2024-12-28)


### Features

* カバー画像とアイコンの指定を可能にする ([daab1af](https://github.com/koboriakira/python-lotion/commit/daab1af621dfb2deec3bd5ae4e7d4844368ea975))


### Bug Fixes

* 使わない関数を削除 ([c9dd4b2](https://github.com/koboriakira/python-lotion/commit/c9dd4b20e5f7cc6323639736d8a3b3fa3e29c189))

## [0.8.1](https://github.com/koboriakira/python-lotion/compare/v0.8.0...v0.8.1) (2024-12-27)


### Features

* fetch_multi_select関数を改善 ([729fa76](https://github.com/koboriakira/python-lotion/commit/729fa76f9f1cfb4f0fa734a19f19d638b572c649))
* fetch_select関数を改善 ([d1ce7a5](https://github.com/koboriakira/python-lotion/commit/d1ce7a527b137b8c6ec82f333884706cbf5dc60a))
* ページの作成状況によって関数を呼び出し分ける ([a3beedd](https://github.com/koboriakira/python-lotion/commit/a3beedd95da305d9ff11bf6fe44208f3232e3cba))

## [0.8.0](https://github.com/koboriakira/python-lotion/compare/v0.7.1...v0.8.0) (2024-12-27)


### ⚠ BREAKING CHANGES

* アノテーションを利用して独自プロパティ、ページを作成できるようにする ([#48](https://github.com/koboriakira/python-lotion/issues/48))

### Features

* アノテーションを利用して独自プロパティ、ページを作成できるようにする ([#48](https://github.com/koboriakira/python-lotion/issues/48)) ([64efa31](https://github.com/koboriakira/python-lotion/commit/64efa31c3cbd9f5287766b890529a63df9ffdd19))

## [0.7.1](https://github.com/koboriakira/python-lotion/compare/v0.7.0...v0.7.1) (2024-12-27)


### Features

* BasePageを継承可能なものにする ([#44](https://github.com/koboriakira/python-lotion/issues/44)) ([a327e56](https://github.com/koboriakira/python-lotion/commit/a327e56e7500e41d21d54e412550df4917f7a393))
* 各プロパティを継承可能にする ([#47](https://github.com/koboriakira/python-lotion/issues/47)) ([4659ad0](https://github.com/koboriakira/python-lotion/commit/4659ad03f0e2759724df28caec4523ef2e02ff9a))

## [0.7.0](https://github.com/koboriakira/python-lotion/compare/v0.6.4...v0.7.0) (2024-12-25)


### ⚠ BREAKING CHANGES

* Titleプロパティの扱いを改善 ([#40](https://github.com/koboriakira/python-lotion/issues/40))

### Features

* Titleプロパティの扱いを改善 ([#40](https://github.com/koboriakira/python-lotion/issues/40)) ([64dff55](https://github.com/koboriakira/python-lotion/commit/64dff55f4119b92db2a91ddec109089bcf29ca73))

## [0.6.4](https://github.com/koboriakira/python-lotion/compare/v0.6.3...v0.6.4) (2024-12-24)


### Features

* BasePageのコピー関数を追加 ([018a16c](https://github.com/koboriakira/python-lotion/commit/018a16c5a17c4adc134250ed7d142619bc48aa30))


### Bug Fixes

* ページ新規作成時にも使わないプロパティは取り除く ([cc18c8c](https://github.com/koboriakira/python-lotion/commit/cc18c8c5b206aa711254009c9210a0d2928b0c79))

## [0.6.3](https://github.com/koboriakira/python-lotion/compare/v0.6.2...v0.6.3) (2024-12-21)


### Features

* 見出しブロックにリッチテキストを指定可能にする ([97733e1](https://github.com/koboriakira/python-lotion/commit/97733e1eeee4c584782a32b4f7790141b3f2b166))

## [0.6.2](https://github.com/koboriakira/python-lotion/compare/v0.6.1...v0.6.2) (2024-12-21)


### Features

* 日付メンションに対応 ([8197bca](https://github.com/koboriakira/python-lotion/commit/8197bca585832a50cecec774a7f3913d1a8bc4fb))

## [0.6.1](https://github.com/koboriakira/python-lotion/compare/v0.6.0...v0.6.1) (2024-12-21)


### Features

* ファイルの操作に対応 ([3342cbf](https://github.com/koboriakira/python-lotion/commit/3342cbf15e3e9f682efab4dfdb7989c4a5a3a57d))
* 受け取ったページのデータからBasePageを作成できる ([f99009b](https://github.com/koboriakira/python-lotion/commit/f99009b0ccf97754fa3e7ac24b0978330c70002a))


### Bug Fixes

* IS_EMPTYのときは文字列チェックをしない ([1bc48e8](https://github.com/koboriakira/python-lotion/commit/1bc48e8830abeb286d1a4290733cc0c547d65f56))
* PageIdを隠蔽する ([#34](https://github.com/koboriakira/python-lotion/issues/34)) ([545ea62](https://github.com/koboriakira/python-lotion/commit/545ea624605c5ef42a3c15b83876c234211c788b))
* Titleインスタンスの生成でPageIdを利用しない ([c7bf7c6](https://github.com/koboriakira/python-lotion/commit/c7bf7c67f21c7246c57b0426787904f638d99be9))

## [0.5.0](https://github.com/koboriakira/lotion/compare/v0.4.0...v0.5.0) (2024-12-15)


### Features

* 作成日時などの更新に対応 ([#29](https://github.com/koboriakira/lotion/issues/29)) ([6daa2e9](https://github.com/koboriakira/lotion/commit/6daa2e97d134a807c69f24b30293e72c5a4b64ce))

## [0.4.0](https://github.com/koboriakira/lotion/compare/v0.3.0...v0.4.0) (2024-12-15)


### Features

* プロパティを空欄で更新できる ([#26](https://github.com/koboriakira/lotion/issues/26)) ([7f2f999](https://github.com/koboriakira/lotion/commit/7f2f9993a1ad4648ddeb102d3923963a1e3d0d8f))

## [0.3.0](https://github.com/koboriakira/lotion/compare/v0.2.0...v0.3.0) (2024-12-15)


### Features

* ユニークIDに対応 ([#23](https://github.com/koboriakira/lotion/issues/23)) ([566eae0](https://github.com/koboriakira/lotion/commit/566eae0461a9bde6542c9dbc6cdbf7a71dd58e74))
* ロールアップのあるページに対応 ([#22](https://github.com/koboriakira/lotion/issues/22)) ([ab0ce93](https://github.com/koboriakira/lotion/commit/ab0ce93422eb2d1a8cbc81a10ad333a9fd897ec3))
* 数式プロパティの入ったページを操作可能にする ([#20](https://github.com/koboriakira/lotion/issues/20)) ([d3709df](https://github.com/koboriakira/lotion/commit/d3709dfabc2bb6c1e085e8c6fb38390b78793ba4))

## [0.2.0](https://github.com/koboriakira/lotion/compare/v0.1.0...v0.2.0) (2024-12-14)


### Features

* マルチセレクトを指定できるようにする ([#16](https://github.com/koboriakira/lotion/issues/16)) ([312b39e](https://github.com/koboriakira/lotion/commit/312b39ee18730bb4a5e510f483c940316f8e09b2))
* 名前を指定してセレクトを取得して利用する ([#14](https://github.com/koboriakira/lotion/issues/14)) ([9a14d4c](https://github.com/koboriakira/lotion/commit/9a14d4cb1ff1135085e44df45b734af230ab80a8))

## 0.1.0 (2024-12-14)


### Bug Fixes

* 正しいキャメルケースに修正 ([#12](https://github.com/koboriakira/lotion/issues/12)) ([9ffbb91](https://github.com/koboriakira/lotion/commit/9ffbb91cfc0c22bdcecf607e5055b052b53e0e61))
