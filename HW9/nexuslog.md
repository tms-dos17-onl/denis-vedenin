2023-08-19 19:50:40,995+0300 INFO  [FelixStartLevel]  *SYSTEM org.sonatype.nexus.internal.orient.DatabaseServerImpl - Activated

2023-08-19 19:50:41,227+0300 INFO  [FelixStartLevel]  *SYSTEM org.sonatype.nexus.extender.NexusLifecycleManager - Start RESTORE

2023-08-19 19:50:41,446+0300 WARN  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Storage 'config' was not closed properly. Will try to recover from write ahead log...

2023-08-19 19:50:41,447+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Looking for last checkpoint...

2023-08-19 19:50:41,461+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} FULL checkpoint found.

2023-08-19 19:50:41,463+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Data restore procedure from full checkpoint is started. Restore is performed from LSN LSN{segment=4, position=28}

2023-08-19 19:50:41,466+0300 WARN  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Record com.orientechnologies.orient.core.storage.impl.local.paginated.wal.OCheckpointEndRecord{lsn=LSN{segment=4, position=52}} will be skipped during data restore

2023-08-19 19:50:41,467+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} 1 operations were processed, current LSN is LSN{segment=4, position=52} last LSN is LSN{segment=4, position=331196}

2023-08-19 19:50:41,478+0300 WARN  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Non tx operation was used during data modification we will need index rebuild.

2023-08-19 19:50:42,176+0300 INFO  [FelixStartLevel]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - Storage 'plocal:/opt/nexus/sonatype-work/nexus3/db/component' is opened under OrientDB distribution : 2.2.36 (build d3beb772c02098ceaea89779a7afd4b7305d3788, branch 2.2.x)

2023-08-19 19:50:42,912+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=config}} Storage data recover was completed

2023-08-19 19:50:43,187+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - Storage 'plocal:/opt/nexus/sonatype-work/nexus3/db/config' is opened under OrientDB distribution : 2.2.36 (build d3beb772c02098ceaea89779a7afd4b7305d3788, branch 2.2.x)

2023-08-19 19:50:43,421+0300 INFO  [ForkJoinPool.commonPool-worker-1]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared - $ANSI{green {db=config}} Wait till indexes restore after crash was finished.

2023-08-19 19:50:43,798+0300 WARN  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Storage 'security' was not closed properly. Will try to recover from write ahead log...

2023-08-19 19:50:43,799+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Looking for last checkpoint...

2023-08-19 19:50:43,800+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} FULL checkpoint found.

2023-08-19 19:50:43,801+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Data restore procedure from full checkpoint is started. Restore is performed from LSN LSN{segment=4, position=28}

2023-08-19 19:50:43,802+0300 WARN  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Record com.orientechnologies.orient.core.storage.impl.local.paginated.wal.OCheckpointEndRecord{lsn=LSN{segment=4, position=52}} will be skipped during data restore

2023-08-19 19:50:43,803+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} 1 operations were processed, current LSN is LSN{segment=4, position=52} last LSN is LSN{segment=4, position=341592}

2023-08-19 19:50:43,804+0300 WARN  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Non tx operation was used during data modification we will need index rebuild.

2023-08-19 19:50:43,808+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Start creation of index 'OUser.name'

2023-08-19 19:50:44,442+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Index 'OUser.name' was successfully created and rebuild is going to be started

2023-08-19 19:50:45,713+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - $ANSI{green {db=security}} Storage data recover was completed

2023-08-19 19:50:46,187+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.storage.impl.local.paginated.OLocalPaginatedStorage - Storage 'plocal:/opt/nexus/sonatype-work/nexus3/db/security' is opened under OrientDB distribution : 2.2.36 (build d3beb772c02098ceaea89779a7afd4b7305d3788, branch 2.2.x)

2023-08-19 19:50:46,223+0300 INFO  [ForkJoinPool.commonPool-worker-2]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared - $ANSI{green {db=security}} Wait till indexes restore after crash was finished.

2023-08-19 19:50:46,599+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexRebuildOutputListener - $ANSI{green {db=config}} - Rebuilding index config.OUser.name (estimated 3 items)...

2023-08-19 19:50:46,615+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexRebuildOutputListener - $ANSI{green {db=config}} --> OK, indexed 3 items in 16 ms

2023-08-19 19:50:47,029+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Start creation of index 'ORole.name'

2023-08-19 19:50:47,566+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Rebuild of 'OUser.name index was successfully finished

2023-08-19 19:50:47,568+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Index 'dictionary' is not automatic index and will be added as is

2023-08-19 19:50:47,569+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Index 'dictionary' was added in DB index list

2023-08-19 19:50:47,945+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Index 'ORole.name' was successfully created and rebuild is going to be started

2023-08-19 19:50:49,018+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Start creation of index 'OFunction.name'

2023-08-19 19:50:50,724+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Index 'OFunction.name' was successfully created and rebuild is going to be started

2023-08-19 19:50:50,777+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexRebuildOutputListener - $ANSI{green {db=security}} - Rebuilding index security.ORole.name (estimated 3 items)...

2023-08-19 19:50:50,787+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexRebuildOutputListener - $ANSI{green {db=security}} --> OK, indexed 3 items in 10 ms

2023-08-19 19:50:51,641+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Rebuild of 'ORole.name index was successfully finished

2023-08-19 19:50:51,642+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Index 'dictionary' is not automatic index and will be added as is

2023-08-19 19:50:51,643+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Index 'dictionary' was added in DB index list

2023-08-19 19:50:52,281+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Start creation of index 'OUser.name'

2023-08-19 19:50:53,271+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=security}} Index 'OUser.name' was successfully created and rebuild is going to be started

2023-08-19 19:50:55,692+0300 INFO  [OrientDB rebuild indexes]  *SYSTEM com.orientechnologies.orient.core.index.OIndexManagerShared$RecreateIndexesTask - $ANSI{green {db=config}} Rebuild of 'OFunction.name index was successfully finished

